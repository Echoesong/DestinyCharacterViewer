from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('bungie_auth/', views.bungie_auth, name='bungie_auth'),
    path('callback/', views.bungie_callback, name='bungie_callback' )
]
