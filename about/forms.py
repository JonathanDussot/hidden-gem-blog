from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    A form for users to submit collaboration requests.
    This form is based on the CollaborateRequest model
    and includes fields for name, email, and message.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
