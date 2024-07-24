from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import SubscriptionInfo, NewsletterSubscription
from .forms import SubscriptionForm

class NewsletterSubscriptionListView(LoginRequiredMixin, ListView):
    model = NewsletterSubscription
    template_name = 'newsletter/newsletter-list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self):
        return NewsletterSubscription.objects.filter(user=self.request.user)

class NewsletterSubscriptionCreateView(CreateView):
    model = NewsletterSubscription
    form_class = SubscriptionForm
    template_name = 'newsletter/newsletter-form.html'
    success_url = reverse_lazy('newsletter-list')

    def form_valid(self, form):
        user = self.request.user if self.request.user.is_authenticated else None
        form.instance.user = user
        email = form.cleaned_data.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.error(self.request, 'This email is already subscribed.')
            return self.form_invalid(form)
        return super().form_valid(form)

class NewsletterSubscriptionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsletterSubscription
    form_class = SubscriptionForm
    template_name = 'newsletter/newsletter-form.html'
    success_url = reverse_lazy('newsletter-list')

    def test_func(self):
        subscription = self.get_object()
        return self.request.user == subscription.user

class NewsletterSubscriptionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsletterSubscription
    template_name = 'newsletter/newsletter-confirm_delete.html'
    success_url = reverse_lazy('newsletter-list')

    def test_func(self):
        subscription = self.get_object()
        return self.request.user == subscription.user

# Updated subscribe_view and unsubscribe_view
def subscribe_view(request):
    subscription_info = get_object_or_404(SubscriptionInfo, id=1)
    user = request.user if request.user.is_authenticated else None

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            subscription, created = NewsletterSubscription.objects.get_or_create(
                email=email,
                defaults={'user': user} if user else {}
            )

            if created:
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed to the newsletter.')
            return redirect('newsletter-list')
        else:
            messages.error(request, 'There was an error with your subscription.')
    else:
        form = SubscriptionForm()

    return render(
        request,
        'newsletter/subscribe.html',
        {
            'SubscriptionInfo': subscription_info,
            'subscription_form': form,
            'user_subscribed': user and NewsletterSubscription.objects.filter(user=user).exists()
        }
    )

def unsubscribe_view(request, email):
    if not email:
        messages.error(request, 'Invalid unsubscribe request.')
        return redirect('newsletter-list')

    try:
        subscription = NewsletterSubscription.objects.get(email=email)
        if subscription.user and request.user != subscription.user:
            messages.error(request, 'You are not authorized to unsubscribe this email.')
            return redirect('newsletter-list')

        subscription.delete()
        messages.success(request, 'You have been unsubscribed successfully.')
    except NewsletterSubscription.DoesNotExist:
        messages.error(request, 'Subscription not found.')

    return redirect('newsletter-list')
