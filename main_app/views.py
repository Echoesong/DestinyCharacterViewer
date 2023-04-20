from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#Oauth 2.0 stuff:
from django.http import HttpResponseRedirect
from django.conf import settings
import uuid
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def bungie_auth(request):
  state = uuid.uuid4()
  request.session['bungie_auth_state'] = str(state)
  auth_url = f"{settings.BUNGIE_AUTHORIZATION_URL}?client_id={settings.BUNGIE_CLIENT_ID}&response_type=code&state={state}"
  return HttpResponseRedirect(auth_url)

def bungie_callback(request):
    print('Bungie callback')
    code = request.GET.get('code')
    state = request.GET.get('state')
    stored_state = request.session.get('bungie_auth_state')

    if state != stored_state:
        return JsonResponse({"error": "Invalid state parameter"})

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": settings.BUNGIE_CLIENT_ID,
        
    }
    response = requests.post(settings.BUNGIE_TOKEN_URL, data=data)
    token_data = response.json()
    membership_id = token_data["membership_id"]
    # Possibly: check if the BungieID exists in our database, if so, don't create/route back. if NOT present, continue below
    # Use token data to make a second request from Bungie API, then create profile

    response2 = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Profile/{membership_id}/LinkedProfiles', headers={'x-api-key': settings.BUNGIE_API_KEY})
    
    destiny2_data = response2.json()
    # NOTE: Eventually need to handle edge case of when existing user tries to connect
    # Profile.objects.create(user=request.user, access_token=token_data['access_token'], token_type=token_data['token_type'], expires_in=token_data['expires_in'], membership_id=token_data['membership_id'], destiny2_membership_id=destiny2_data['profiles'][0]['membershipId'])
    print(destiny2_data)
    print('Request resolved')
    # Instead of redirecting to home, chain this request with the request to get destinyMembershipId
    return redirect('home')


@login_required
def profile(request):
  user_profile = Profile.objects.filter(user=request.user)
  return render(request, 'registration/profile.html', {'user_profile': user_profile})


# def characters_create(request):
#   # NOTE: 
#   user_profile = Profile.objects.filter(user=request.user)
  
#   response = request.GET.get('https://www.bungie.net/Platform/Destiny2/3/Profile/{user_profile['membership_id']}/LinkedProfiles')
#   pass

# def characters_index(request):
   
#    characters = Character.objects.filter(user=request.user)

#    return render(request, 'characters/index.html', {'characters': characters})