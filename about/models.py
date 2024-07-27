"""
Database models for the About app
"""
from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Model representing the 'About' section of the website.
    """

    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """
        Returns title of About section
        """
        return self.title


class CollaborateRequest(models.Model):
    """
    Model representing the collaboration request.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    
    def __str__(self):
        """
        indicates the collaboration request with the user's name.
        """
        return f"Collaboration request from {self.name}"