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
    bearer = token_data['token_type']
    token = token_data['access_token']
    # Possibly: check if the BungieID exists in our database, if so, don't create/route back. if NOT present, continue below
    # Use token data to make a second request from Bungie API, then create profile

    response2 = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Profile/{membership_id}/LinkedProfiles', headers={'x-api-key': settings.BUNGIE_API_KEY})
    
    destiny2_data = response2.json()
    # NOTE: Eventually need to handle edge case of when existing user tries to connect
    destiny2_membership_id = destiny2_data['Response']['profiles'][0]['membershipId']
    Profile.objects.create(
       user=request.user, 
       access_token=token_data['access_token'], 
       token_type=bearer, 
       expires_in=token_data['expires_in'], 
       membership_id=token_data['membership_id'], 
       destiny2_membership_id=destiny2_membership_id)
    print('Request resolved')
    # Instead of redirecting to home, chain this request with the request to get destinyMembershipId
    return redirect('gatheringdata')
    
def gatheringdata(request):
    race1 = Race.objects.get(id=1)
    race2 = Race.objects.get(id=2)
    race3 = Race.objects.get(id=3)

    class1 = Class.objects.get(id=1)
    class2 = Class.objects.get(id=2)
    class3 = Class.objects.get(id=3)

    user_profile = Profile.objects.get(user=request.user)
    destiny2_membership_id = user_profile['destiny2_memebership_id']
    token = user_profile['access_token']

    response3 = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Profile/{destiny2_membership_id}', headers={'x-api-key': settings.BUNGIE_API_KEY, 'Authorization': f'Bearer {token}'}, params={'components': 'characters'})
      
    parsed = response3.json()
    characters = parsed['Response']['characters']['data']
    character_id_list = characters.keys()


    for key in character_id_list:
        character_data = characters[key]
        if character_data['raceType'] == 0:
          character_race = race1
        elif character_data['raceType'] == 1:
          character_race = race2
        elif character_data['raceType'] == 2:
          character_race = race3

        if character_data['classType'] == 0:
          character_class = class1
        elif character_data['classType'] == 1:
          character_class = class2
        elif character_data['classType'] == 2:
          character_class = class3

        Character.objects.create(
            user = request.user,
            light = character_data['light'],
            total_minutes = character_data['minutesPlayedTotal'],
            session_minutes = character_data['minutesPlayedThisSession'],
            last_played = character_data['dateLastPlayed'],
            emblem_icon = character_data['emblemPath'],
            emblem_background = character_data['emblemBackgroundPath'],
            race_type = character_race,
            class_type = character_class

        )

      

    print('Request resolved')
    # Instead of redirecting to home, chain this request with the request to get destinyMembershipId
    return render(request, 'gatheringdata')


@login_required
def profile(request):
  user_profile = Profile.objects.filter(user=request.user)
  return render(request, 'registration/profile.html', {'user_profile': user_profile})


