from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=255)
    expires_in = models.IntegerField()
    refresh_token = models.CharField(max_length=255, null=True, blank=True)  # This is for confidential clients only
    membership_id = models.CharField(max_length=255)
    
    def __str__(self):
        return f"belongs to {self.user}"