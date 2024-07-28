"""
Functions for the Newsletter app view code
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import SubscriptionInfo, NewsletterSubscription
from .forms import SubscriptionForm


class NewsletterSubscriptionListView(LoginRequiredMixin, ListView):
    """
    Renders list of emails subscribed
    """
    model = NewsletterSubscription
    template_name = 'newsletter/newsletter-list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self):
        return NewsletterSubscription.objects.filter(user=self.request.user)


class NewsletterSubscriptionCreateView(CreateView):
    """
    provides user with form
    """
    model = NewsletterSubscription
    form_class = SubscriptionForm
    template_name = 'newsletter/newsletter-form.html'
    success_url = reverse_lazy('newsletter_list')

    def form_valid(self, form):
        """
        to subscribe with their emails.
        """
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None
        form.instance.user = user
        email = form.cleaned_data.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.error(self.request, 'This email is already subscribed.')
            return self.form_invalid(form)
        return super().form_valid(form)


class NewsletterSubscriptionUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                                       UpdateView):
    """
    checks logged in user's information and provides user with form
    """
    model = NewsletterSubscription
    form_class = SubscriptionForm
    template_name = 'newsletter/newsletter-form.html'
    success_url = reverse_lazy('newsletter_list')

    def test_func(self):
        """
        to update their email
        """
        subscription = self.get_object()
        return self.request.user == subscription.user


class NewsletterSubscriptionDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                                       DeleteView):
    """
    provides user with option to delete email
    """
    model = NewsletterSubscription
    template_name = 'newsletter/newsletter-confirm-delete.html'
    success_url = reverse_lazy('newsletter_list')

    def test_func(self):
        """
        Delete subscription
        """
        subscription = self.get_object()
        return self.request.user == subscription.user


def subscribe_view(request):
    """
    provides user with form and validates they are logged in to
    subscribe to a form and renders a message back.
    """
    subscription_info = get_object_or_404(SubscriptionInfo, id=1)
    user = request.user if request.user.is_authenticated else None

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            subscription, created = (
                NewsletterSubscription.objects.get_or_create(
                    email=email,
                    defaults={'user': user} if user else {}
                )
            )

            if created:
                messages.success(request,
                                 'Thank you for subscribing to our'
                                 + ' newsletter!')
            else:
                messages.info(request, 'You are already subscribed to the'
                              + ' newsletter.')
            return redirect('newsletter_list')
        else:
            messages.error(request, 'There was an error with your'
                           + 'subscription.')
    else:
        form = SubscriptionForm()

    return render(
        request,
        'newsletter/subscribe.html',
        {
            'SubscriptionInfo': subscription_info,
            'subscription_form': form,
            'user_subscribed': user and
            NewsletterSubscription.objects.filter(user=user).exists()
        }
    )


def unsubscribe_view(request, email):
    """
    provides user with option to unsubscribe and validates they are
    the correct user based on login, renders a message back.
    """
    if not email:
        messages.error(request, 'Invalid unsubscribe request.')
        return redirect('newsletter_list')

    try:
        subscription = NewsletterSubscription.objects.get(email=email)
        if subscription.user and request.user != subscription.user:
            messages.error(request, 'You are not authorized to unsubscribe'
                           + ' this email.')
            return redirect('newsletter_list')

        subscription.delete()
        messages.success(request, 'You have been unsubscribed successfully.')
    except NewsletterSubscription.DoesNotExist:
        messages.error(request, 'Subscription not found.')

    return redirect('newsletter_list')
