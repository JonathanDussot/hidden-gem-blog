from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    A form for users to submit comments on blog posts.
    This form is based on the comment model
    and includes fields for body.
    """
    class Meta:
        model = Comment
        fields = ('body',)
