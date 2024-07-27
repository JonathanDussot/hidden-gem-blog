from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.
    Uses Summernote for rich text editing in the content field.
    """
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CollaborateRequest model.
    Displays 'message' and 'read' fields in the list view.
    """
    list_display = ('message', 'read',)
