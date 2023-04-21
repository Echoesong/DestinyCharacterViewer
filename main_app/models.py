from django.db import models
from django.contrib.auth.models import User
from enum import Enum

# Create your models here.

SUBCLASSES = ('Solar', 'Void', 'Arc', 'Stasis', 'Strand') 
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500)
    token_type = models.CharField(max_length=500)
    expires_in = models.IntegerField()
     
    membership_id = models.CharField(max_length=500)
    destiny2_membership_id = models.CharField(max_length=500)

    def __str__(self):
        return f"belongs to {self.user}"
    
# WEAPON_SLOTS = (
#     ('Kin', 'Kinetic'),
#     ('En', 'Energy'),
#     ('Hev', 'Heavy')
# )

# ARMOR_SLOTS = (
#     ('H', 'Kinetic'),
#     ('A', 'Arms'),
#     ('Ch', 'Chest'),
#     ('L', 'Legs'),
#     ('Cl', 'Class')
# )


# class Weapon(models.Model):
#     id = models.IntegerField
#     # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     # instance_id = models.IntegerField()
#     name = models.CharField(max_length=100)
#     icon = models.CharField(max_length=100)
#     # NOTE: default probably doesn't work for the app, as defaulting to that index location is nonsensical. Keeping for now
#     slot = models.CharField(max_length=3, choices=WEAPON_SLOTS, default=WEAPON_SLOTS[0][0])

#     def __str__(self):
#         return self.name

# class Armor(models.Model):
#     id = models.IntegerField
#     # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     # instance_id = models.IntegerField()
#     name = models.CharField(max_length=100)
#     icon = models.CharField(max_length=100)
#     # NOTE: ref: note in class Weapon
#     slot = models.CharField(max_length=100, choices=ARMOR_SLOTS, default=ARMOR_SLOTS[0][0])

#     def __str__(self):
#       return self.name
    


# class Ability(models.Model):
#     bungie_api_ability_id = models.IntegerField()
#     name = models.CharField(max_length=255)
#     icon = models.CharField(max_length=255)
#     subclass = models.CharField(max_length=6,
#                             choices = SUBCLASSES,
#                             default = SUBCLASSES[0])


# class Loadout(models.Model):
#     character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     abilities = models.ManyToManyField(Ability)
#     #there is no on_delete, do we need a different method than cascade for this?
#     weapon_kinetic = models.ForeignKey(Weapon)
#     weapon_energy = models.ForeignKey(Weapon)
#     weapon_heavy = models.ForeignKey(Weapon)
#     armor_head = models.ForeignKey(Armor)
#     armor_shoulder = models.ForeignKey(Armor)
#     armor_chest = models.ForeignKey(Armor)
#     armor_legs = models.ForeignKey(Armor)
#     armor_class = models.ForeignKey(Armor)

