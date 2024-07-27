from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for managing Blog Posts in the Django admin interface.

    - Displays the following fields in the list view: title, slug, status,
     and created_on.
    - Allows searching for posts by title and content.
    - Provides filtering options based on post status and creation date.
    - Automatically populates the 'slug' field using the post title.
    - Integrates Summernote for rich text editing in the 'content' field.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
