# Generated by Django 3.0 on 2019-12-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('x', models.DecimalField(blank=True, decimal_places=10, default=None, help_text='Latitude Coordinate', max_digits=1007)),
                ('y', models.DecimalField(blank=True, decimal_places=10, default=None, help_text='Longitude Coordinate', max_digits=1006)),
                ('unique_squirrel_id', models.CharField(blank=True, default=None, max_length=14, primary_key=True, serialize=False)),
                ('hectare', models.CharField(blank=True, default=None, max_length=3)),
                ('shift', models.CharField(blank=True, default=None, max_length=2)),
                ('date', models.CharField(blank=True, default=0, max_length=20)),
                ('hectare_squirrel_number', models.IntegerField(blank=True, default=0)),
                ('age', models.CharField(blank=True, default=None, max_length=8)),
                ('primary_fur_color', models.CharField(blank=True, default=None, max_length=8)),
                ('highlight_fur_color', models.CharField(blank=True, default=None, max_length=8)),
                ('combination_of_primary_and_highlight_color', models.CharField(blank=True, default=None, max_length=100)),
                ('color_notes', models.CharField(blank=True, default=None, max_length=100)),
                ('location', models.CharField(blank=True, default=None, max_length=100)),
                ('above_ground_sighter_measurement', models.CharField(blank=True, default=None, max_length=10)),
                ('specific_location', models.CharField(blank=True, default=None, help_text='specific location of squirrel', max_length=100)),
                ('running', models.BooleanField(blank=True, default=None, help_text='whether the squirrel is running')),
                ('chasing', models.BooleanField(blank=True, default=None, help_text='whether the squirrel is chasing')),
                ('climbing', models.BooleanField(blank=True, default=None, help_text='whether the squirrel is climbing')),
                ('eating', models.BooleanField(blank=True, default=None, help_text='whether the squirrel is eating')),
                ('foraging', models.BooleanField(blank=True, default=None, help_text='whether the squirrel is foraging')),
                ('other_activities', models.CharField(blank=True, default=None, max_length=100)),
                ('kuks', models.BooleanField(blank=True, default=None, help_text='whether the squirrel kuks')),
                ('quaas', models.BooleanField(blank=True, default=None, help_text='whether the squirrel quaas')),
                ('moans', models.BooleanField(blank=True, default=None, help_text='whether the squirrel moans')),
                ('tail_flags', models.BooleanField(blank=True, default=None, help_text='whether the squirrel has tail flags')),
                ('tail_twitches', models.BooleanField(blank=True, default=None, help_text='whether the squirrel has tail twitches')),
                ('approaches', models.BooleanField(blank=True, default=None, help_text='whether the squirrel approaches')),
                ('indifferent', models.BooleanField(blank=True, default=None, help_text='whether the squirrel is indifferent')),
                ('runs_from', models.BooleanField(blank=True, default=None, help_text='whether the squirrel runs from')),
                ('other_interactions', models.CharField(blank=True, default=None, max_length=100)),
                ('lat_long', models.CharField(blank=True, default=None, max_length=100)),
                ('zip_codes', models.CharField(blank=True, default=None, max_length=100)),
                ('community_districts', models.IntegerField(blank=True, default=0)),
                ('borough_boundaries', models.IntegerField(blank=True, default=0)),
                ('city_coucil_districts', models.IntegerField(blank=True, default=0)),
                ('police_precincts', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]