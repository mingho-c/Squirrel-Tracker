from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    x = models.DecimalField(
            max_digits=1007, decimal_places=10, default=None, blank=True,
            help_text=_('Latitude Coordinate'),
            )

    y = models.DecimalField(
            max_digits=1006, decimal_places=10, default=None, blank=True,
            help_text=_('Longitude Coordinate'),
            )

    unique_squirrel_id = models.CharField(
            max_length=14, default=None, primary_key=True, blank=True,
            )
    
    hectare = models.CharField(
            max_length=3, default=None, blank=True,
            )

    shift = models.CharField(
            max_length=2, default=None, blank=True,
            )

    date = models.CharField(
            max_length=20, default=0, blank=True,
            )

    hectare_squirrel_number = models.IntegerField(
            default=0, blank=True,
            )

    age = models.CharField(
            max_length=8, default=None, blank=True,
            )

    primary_fur_color = models.CharField(
            max_length=8, default=None, blank=True,
            )

    highlight_fur_color = models.CharField(
            max_length=8, default=None, blank=True,
            )

    combination_of_primary_and_highlight_color = models.CharField(
            max_length=100, default=None, blank=True,
            )

    color_notes = models.CharField(
            max_length=100, default=None, blank=True,
            )

    location = models.CharField(
            max_length=100, default=None, blank=True,
            )

    above_ground_sighter_measurement = models.CharField(
            max_length=10, default=None, blank=True,
            )

    specific_location = models.CharField(
            max_length=100, default=None, blank=True,
            help_text=_('specific location of squirrel'),
            )

    running = models.BooleanField(
            default=None, 
            blank=True,
            help_text=_('whether the squirrel is running'),
            )

    chasing = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel is chasing'),
            )

    climbing = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel is climbing'),
            )

    eating = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel is eating'),
            )

    foraging = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel is foraging'),
            )

    other_activities = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    kuks = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel kuks'),
            )

    quaas = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel quaas'),
            )

    moans = models.BooleanField(
            default=None,
            blank=True,
            help_text=_('whether the squirrel moans'),
            )

    tail_flags = models.BooleanField(
            default=None,
            blank=True,
            help_text = _('whether the squirrel has tail flags'),
            )

    tail_twitches = models.BooleanField(
            default=None,
            blank=True,
            help_text = _('whether the squirrel has tail twitches'),
            )

    approaches = models.BooleanField(
            default=None,
            blank=True,
            help_text = _('whether the squirrel approaches'),
            )

    indifferent = models.BooleanField(
            default=None,
            blank=True,
            help_text = _('whether the squirrel is indifferent'),
            )

    runs_from = models.BooleanField(
            default=None,
            blank=True,
            help_text = _('whether the squirrel runs from'),
            )

    other_interactions = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    lat_long = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    zip_codes = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    community_districts = models.IntegerField(
            default=0,
            blank=True,
            )

    borough_boundaries = models.IntegerField(
            default=0,
            blank=True,
            )

    city_coucil_districts = models.IntegerField(
            default=0,
            blank=True,
            )

    police_precincts = models.IntegerField(
            default=0,
            blank=True,
            )
