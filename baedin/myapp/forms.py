from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Permission
from django.core import validators

from . import models

RACE_CHOICES = (('Human','Human'),('Dwarf','Dwarf'),('Elf','Elf'),('Gnome','Gnome'),('Dragonborn','Dragonborn'),
('Halfling','Halfling'),('Tiefling','Tiefling'),('Goblin','Goblin'),('Orc','Orc'),('Turtle','Turtle'))

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    return value

def is_valid_race_option(value):
    flag = False
    for tup in RACE_CHOICES:
        if value in tup:
            flag = True
    if flag == False:
        raise forms.ValidationError("Not a valid option")
    return value

class CharacterForm(forms.Form):
    name = forms.CharField(
    label="Character Name",
    required=True,
    max_length=64
    )
    description = forms.CharField(
    label="Character Description",
    required=True,
    max_length=256,
    )
    race = forms.Field(
    label="Race",
    widget=forms.Select(choices=RACE_CHOICES),
    required=False,
    validators=[is_valid_race_option]
    )
    weapon = forms.CharField(
    label="Weapon",
    required=False,
    max_length=32
    )
    strength = forms.IntegerField(
    label="Strength Score",
    required=True,
    validators=[validators.MinValueValidator(1),validators.MaxValueValidator(20)]
    )
    dexterity = forms.IntegerField(
    label="Dexterity Score",
    required=True,
    validators=[validators.MinValueValidator(1),validators.MaxValueValidator(20)]
    )
    wisdom = forms.IntegerField(
    label="Wisdom Score",
    required=True,
    validators=[validators.MinValueValidator(1),validators.MaxValueValidator(20)]
    )
    intelligence = forms.IntegerField(
    label="Intelligence Score",
    required=True,
    validators=[validators.MinValueValidator(1),validators.MaxValueValidator(20)]
    )
    charisma = forms.IntegerField(
    label="Charisma Score",
    required=True,
    validators=[validators.MinValueValidator(1),validators.MaxValueValidator(20)]
    )

    def save(self, request):
        character_instance = models.CharacterModel()
        character_instance.name = self.cleaned_data["name"]
        character_instance.description = self.cleaned_data["description"]
        character_instance.player_id = request.user
        character_instance.race = self.cleaned_data["race"]
        character_instance.weapon = self.cleaned_data["weapon"]
        character_instance.strength = self.cleaned_data["strength"]
        character_instance.dexterity = self.cleaned_data["dexterity"]
        character_instance.wisdom = self.cleaned_data["wisdom"]
        character_instance.intelligence = self.cleaned_data["intelligence"]
        character_instance.charisma = self.cleaned_data["charisma"]
        # perm = Permission.objects.get(name='has character')
        # User.user_permissions.add(perm)
        character_instance.save()
        return character_instance

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
