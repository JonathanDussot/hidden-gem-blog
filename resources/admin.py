from django.contrib import admin
from .models import Resources
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Resources)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content_one', 'content_two', 'content_three',)