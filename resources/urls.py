"""
URL paths to render each view to the browser.
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.travel_resources, name='resources'),
]
