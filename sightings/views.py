from django.shortcuts import render
from django.http import HttpResponse
from sightings.models import Squirrel

def all(request):
    squirrels = Squirrel.objects.all()
    context = {
            's': squirrels,
            }
    return render(request, 'sightings/all.html', context)
