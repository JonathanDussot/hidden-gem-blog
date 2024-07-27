"""
Database models for the Resources app.
"""
from django.db import models
from cloudinary.models import CloudinaryField


class Resources(models.Model):
    """
    Model representing the resources section
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content_one = models.TextField(default='Default content for content one')
    content_two = models.TextField(default='Default content for content two')
    content_three = models.TextField(default='Default content for content'
                                     + ' three')

    def __str__(self):
        """
        Returns title
        """
        return self.title
