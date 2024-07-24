# newsletter/urls.py
from django.urls import path
from . import views  # Import views here

urlpatterns = [
    path('subscribe/', views.subscribe_view, name='subscribe_to_newsletter'),
    path('unsubscribe/<str:email>/', views.unsubscribe_view, name='unsubscribe_from_newsletter'),
]
