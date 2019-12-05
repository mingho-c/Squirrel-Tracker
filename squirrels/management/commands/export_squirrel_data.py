import csv

from django.core.management.base import BaseCommand
from squirrels.models import Squirrel 

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *args, **options):
        meta = {
            'file': args[0],
            'class': squirrel,
            'fields': (
                'x',
                'y',
                'unique_squirrel_id',
                'hectare',
                'shift',
                'date',
                'hectare_squirrel_number',
                'age',
                'primary_fur_color',
                'highlight_fur_color',
                'combination_of_primary_and_highlight_color',
                'color_notes',
                'location',
                'above_ground_sighter_measurement',
                'specific_location',
                'running',
                'chasing',
                'climbing',
                'eating',
                'foraging',
                'other_activities',
                'kuks',
                'quaas',
                'moans',
                'tail_flags',
                'tail_twitches',
                'approaches',
                'indifferent',
                'runs_from',
                'other_interactions',
                'lat_long',
                'zip_codes',) 
        }
        f = open(meta['file'], 'w+')
        writer = csv.writer(f)
        writer.writerow( meta['fields'] )
        for obj in meta['class'].objects.all():
            row = [getattr(obj, field) for field in meta['fields']]
            writer.writerow(row)
        f.close()
