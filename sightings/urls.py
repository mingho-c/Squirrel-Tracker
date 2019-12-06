from django.urls import path
from . import views
urlpatterns=[
        path('map/',views.map),
        path('sightings/',views.all),
        path('sightings/<str:squirrel_id>/',views.editsightings),
]
