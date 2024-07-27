from django.contrib import admin
from .models import Resources
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resources)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Resources model.

    Uses Summernote for rich text editing in each of the three content
    fields.
    """

    summernote_fields = ('content_one', 'content_two', 'content_three',)
