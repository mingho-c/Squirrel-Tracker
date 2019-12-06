from django.urls import path
from . import views
urlpatterns = [
        path('add/', views.add),
        path('map/', views.map),
        path('sightings/', views.all),
        path('sightings/<str:squirrel_id>/', views.edit),
]
