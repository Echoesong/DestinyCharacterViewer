from django.urls import path, include 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('bungie_auth/', views.bungie_auth, name='bungie_auth'),
    path('callback/', views.bungie_callback, name='bungie_callback' ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('gatheringdata/', views.gatheringdata, name='gatheringdata')
    
 
]
