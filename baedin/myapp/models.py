from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

class CharacterModel(models.Model):
    class Meta:
        permissions = (
        ("has_character", "has character"),
        )
    name = models.CharField(max_length=64)
    player_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    race = models.CharField(default='Human',max_length=24)
    weapon = models.CharField(default='Fists',max_length=32)
    strength = models.IntegerField(default=random.randint(1,20))
    dexterity = models.IntegerField(default=random.randint(1,20))
    wisdom = models.IntegerField(default=random.randint(1,20))
    intelligence = models.IntegerField(default=random.randint(1,20))
    charisma = models.IntegerField(default=random.randint(1,20))
    
    def __str__(self):
        " " + str(self.name) + " " + str(self.description)
