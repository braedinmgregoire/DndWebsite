from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timezone
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register_view(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()

    context = {
        "title":"Registration",
        "form":form_instance
    }
    return render(request, "registration/register.html", context=context)

@login_required
def character_view(request):
    if request.method== "POST":
        character_form = forms.CharacterForm(request.POST, request.FILES)
        if character_form.is_valid():
            character_form.save(request)
            return redirect("/")
    else:
        character_form = forms.CharacterForm()
    context = {
        "title":"Add Your Character!",
        "form":character_form,
    }
    return render(request, "character.html", context=context)

rolls = (("Acrobatics", "DEX"),("Animal Handling", "WIS"),("Arcana", "INT"),("Athletics", "STR"),("Deception", "CHA"),
("History", "INT"),("Insight", "WIS"),("Intimidation", "CHA"),("Investigation", "INT"),("Medicine", "WIS"),("Nature", "INT"),
("Perception", "WIS"),("Performance", "CHA"),("Persuasion", "CHA"),("Religion", "INT"),("Sleight of Hand", "DEX"),("Stealth", "DEX"),("Survival", "WIS"))
@login_required
def functions_view(request):
    context = {
        "title":"Interact with your Character!",
        "rolls": rolls,
    }
    return render(request, "functions.html", context=context)

# Create your views here.
def index(request):
    context = {
        "title": "CINS 465 Title",
        "variable": "CINS465 Hello World"
    }
    return render(request, "index.html", context=context)
    #return HttpResponse("CINS465 Hello World")

def home(request):
    if request.user.is_authenticated:
        exists = models.CharacterModel.objects.filter(player_id=request.user).exists()
    else:
        exists = False
    context = {
        "title": "Homepage",
        "exists": exists,
    }
    return render(request, "home.html", context=context)

def about(request):
    context = {
    "title": "about",
    }
    return render(request, "about.html", context=context)

def characters_view(request):
    character_objects = models.CharacterModel.objects.all().order_by('-name')
    characters = {}
    characters["characters"] = []
    for charz in character_objects:
        temp_char = {}
        temp_char["description"] = charz.description
        temp_char["name"] = charz.name
        temp_char["race"] = charz.race
        temp_char["weapon"] = charz.weapon
        characters["characters"] += [temp_char]
    return JsonResponse(characters)

def functionz_view(request):
    character_object = models.CharacterModel.objects.all().get(player_id = request.user)
    the_character = {}
    the_character["description"] = character_object.description
    the_character["name"] = character_object.name
    the_character["race"] = character_object.race
    the_character["weapon"] = character_object.weapon
    the_character["strength"] = character_object.strength
    the_character["wisdom"] = character_object.wisdom
    the_character["charisma"] = character_object.charisma
    the_character["dexterity"] = character_object.dexterity
    the_character["intelligence"] = character_object.intelligence
    return JsonResponse(the_character)

@login_required
def tavern(request):
    return render(request, 'tavern.html')

@login_required
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
