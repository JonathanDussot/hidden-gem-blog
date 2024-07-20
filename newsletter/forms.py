from django import forms
from .models import NewsletterSubscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']