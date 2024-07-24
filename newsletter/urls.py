from django.urls import path
from .views import (
    NewsletterSubscriptionListView,
    NewsletterSubscriptionCreateView,
    NewsletterSubscriptionUpdateView,
    NewsletterSubscriptionDeleteView,
    subscribe_view,
    unsubscribe_view,
)

urlpatterns = [
    path('', NewsletterSubscriptionListView.as_view(), name='newsletter_list'),
    path('subscribe/', NewsletterSubscriptionCreateView.as_view(), name='newsletter_subscribe'),
    path('subscribe-form/', subscribe_view, name='subscribe_to_newsletter'),  # for form handling
    path('unsubscribe/<str:email>/', unsubscribe_view, name='unsubscribe_from_newsletter'),
    path('<int:pk>/update/', NewsletterSubscriptionUpdateView.as_view(), name='newsletter_update'),
    path('<int:pk>/delete/', NewsletterSubscriptionDeleteView.as_view(), name='newsletter_delete'),
]
