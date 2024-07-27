from django import forms
from .models import NewsletterSubscription


class SubscriptionForm(forms.ModelForm):
    """
    A form for subscribing to the newsletter. This form allows users to enter
    their email address to subscribe. It also handles associating a user with
    the subscription if provided.
    """
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def __init__(self, *args, **kwargs):
        """
        Initializes the form. Accepts an optional 'user' argument to associate
        the subscription with a specific user.

        Args:
            *args: Variable length argument list.
            **kwargs: Keyword arguments, where 'user' can be provided to
            associate with the form.
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Saves the form data to the database. Associates the subscription with
        a user if one is provided.

        Args:
            commit (bool): Whether to save the instance to the database.
            Defaults to True.

        Returns:
            NewsletterSubscription: The saved subscription instance.
        """
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
