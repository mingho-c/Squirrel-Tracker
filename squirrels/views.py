from django.shortcuts import render
from django.http import HttpResponse
from squirrels.models import Squirrel

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            's': squirrels,
            }
    return render(request, 'squirrels/all.html', context)
