from django.db import models
from django.contrib.auth.models import User
from enum import Enum

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
    
WEAPON_SLOTS = (
    ('Kin', 'Kinetic'),
    ('En', 'Energy'),
    ('Hev', 'Heavy')
)

ARMOR_SLOTS = (
    ('H', 'Kinetic'),
    ('A', 'Arms'),
    ('Ch', 'Chest'),
    ('L', 'Legs'),
    ('Cl', 'Class')
)


class Weapon(models.Model):
    id = models.IntegerField
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # instance_id = models.IntegerField()
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    # NOTE: default probably doesn't work for the app, as defaulting to that index location is nonsensical. Keeping for now
    slot = models.CharField(max_length=3, choices=WEAPON_SLOTS, default=WEAPON_SLOTS[0][0])

    def __str__(self):
        return self.name

class Armor(models.Model):
    id = models.IntegerField
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # instance_id = models.IntegerField()
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    # NOTE: ref: note in class Weapon
    slot = models.CharField(max_length=100, choices=ARMOR_SLOTS, default=ARMOR_SLOTS[0][0])

    def __str__(self):
        return self.name
