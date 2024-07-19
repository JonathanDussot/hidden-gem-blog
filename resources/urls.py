from . import views
from django.urls import path

urlpatterns = [
    path('', views.travel_resources, name='resources'),
]