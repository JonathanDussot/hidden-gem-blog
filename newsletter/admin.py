from django.contrib import admin
from .models import SubscriptionInfo, NewsletterSubscription
from django_summernote.admin import SummernoteModelAdmin


@admin.register(SubscriptionInfo)
class SubscriptionInfoAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(SummernoteModelAdmin):

    list_display = ('email', 'subscribed_on')
    search_fields = ('email',)
    list_filter = ('subscribed_on',)