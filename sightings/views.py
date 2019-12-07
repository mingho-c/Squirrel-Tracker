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
            new = form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm()
    context = {
            'form': form,
                }
    return render(request, 'sightings/add.html', context)

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
            's': squirrels,
            }
    return render(request, 'sightings/map.html', context)

def edit(request, unique_squirrel_id):
    squirrels = Squirrel.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrels)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance = squirrels)
    context = {
            'form': form,
                }
    return render(request, 'sightings/edit.html', context)


def stats(request):
    squirrels = Squirrel.objects.all()
    length = len(squirrels)
    forage_num = sum([1 if s.foraging else 0 for s in squirrels])
    run_num = sum([1 if s.running else 0 for s in squirrels])
    chase_num = sum([1 if s.chasing else 0 for s in squirrels])
    climb_num = sum([1 if s.climbing else 0 for s in squirrels])

    text = f"""
    General Stats of Squirrel Sightings \n\
    Total Number of Squirrels Sightings: {length}\n\
    Total Number of Squirrels Foraging: {forage_num}\n\
    Total Number of Squirrels Running: {run_num}\n\
    Total Number of Squirrels Chasing: {chase_num}\n\
    Total Number of Squirrels Climbing: {climb_num}\n\
    """
    
    return HttpResponse(text, content_type = 'text/plain')
   
