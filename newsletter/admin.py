from django.contrib import admin
from .models import SubscriptionInfo, NewsletterSubscription
from django_summernote.admin import SummernoteModelAdmin


@admin.register(SubscriptionInfo)
class SubscriptionInfoAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the subscription information model.
    Uses Summernote for rich text editing in the content field.
    """

    summernote_fields = ('content',)


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(SummernoteModelAdmin):
    """
    Admin configuration for managing newsletter subscriptions in the Django
    admin interface.

    - Displays the following fields in the list view: email and subscribed_on.
    - Allows searching for posts by email.
    - Provides filtering options based on subscription date.
    """

    list_display = ('email', 'subscribed_on')
    search_fields = ('email',)
    list_filter = ('subscribed_on',)