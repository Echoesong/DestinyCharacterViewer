from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SUBCLASSES = ('Solar', 'Void', 'Arc', 'Stasis', 'Strand') 
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=255)
    expires_in = models.IntegerField()
    refresh_token = models.CharField(max_length=255, null=True, blank=True)  # This is for confidential clients only
    membership_id = models.CharField(max_length=255)
    
    def __str__(self):
        return f"belongs to {self.user}"
    


class Ability(models.Model):
    bungie_api_ability_id = models.IntegerField()
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    subclass = models.CharField(max_length=6,
                            choices = SUBCLASSES,
                            default = SUBCLASSES[0])





















class Loadout(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    abilities = models.ManyToManyField(Ability)
    #there is no on_delete, do we need a different method than cascade for this?
    weapon_kinetic = models.ForeignKey(Weapon)
    weapon_energy = models.ForeignKey(Weapon)
    weapon_heavy = models.ForeignKey(Weapon)
    armor_head = models.ForeignKey(Armor)
    armor_shoulder = models.ForeignKey(Armor)
    armor_chest = models.ForeignKey(Armor)
    armor_legs = models.ForeignKey(Armor)
    armor_class = models.ForeignKey(Armor)