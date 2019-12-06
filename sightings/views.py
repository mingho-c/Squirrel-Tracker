from django.shortcuts import render, redirect
from django.http import HttpResponse
from sightings.models import Squirrel
from sightings.forms import SquirrelForm

def all(request):
    squirrels = Squirrel.objects.all()
    context = {
            's': squirrels,
            }
    return render(request, 'sightings/all.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm()
    context = {
            'f': form,
            }
    return render(request, 'sightings/add.html', context)

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
            "s": squirrels,
    }
    return render(request, 'sightings/map.html', context)

