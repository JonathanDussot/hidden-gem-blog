from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings

# Create your models here.
class SubscriptionInfo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    subscribed_on = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.email
