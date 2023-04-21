from django.db import models
from django.contrib.auth.models import User
from enum import Enum

# Create your models here.


    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500)
    token_type = models.CharField(max_length=500)
    expires_in = models.IntegerField()
     
    membership_id = models.CharField(max_length=500)
    destiny2_membership_id = models.CharField(max_length=500)

    def __str__(self):
        return f"belongs to {self.user}"
    
# class Race:
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)

# class Class:
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)

# class Character(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     light = models.IntegerField()
#     total_minutes = models.IntegerField()
#     session_minutes = models.IntegerField()
#     last_played = models.DateField()
#     emblem_icon = models.CharField(max_length=500)
#     emblem_background = models.CharField(max_length=500)
#     race_type = models.ForeignKey(Race, on_delete=models.CASCADE)
#     class_type = models.ForeignKey(Class, on_delete=models.CASCADE)