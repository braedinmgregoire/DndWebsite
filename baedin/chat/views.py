from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def tavern(request):
    return render(request, 'chat/tavern.html')
