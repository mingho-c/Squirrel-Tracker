from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = 
        
        labels = {
                'x': _('latitude'),
                'y': _('longitude'),
                'unique_squirrel_id': _('unique squirrel id'),
                'primary_fur_color': _('primary fur color'),
                'specific_location': _('specific location'),
                'other_activies': _('other activities'),
                'runs_from': _('runs from'),
                }
