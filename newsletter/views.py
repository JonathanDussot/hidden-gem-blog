from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import SubscriptionInfo, NewsletterSubscription

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
            return redirect('home')
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
        return redirect('home')

    try:
        subscription = NewsletterSubscription.objects.get(email=email)
        if subscription.user and request.user != subscription.user:
            messages.error(request, 'You are not authorized to unsubscribe this email.')
            return redirect('home')

        subscription.delete()
        messages.success(request, 'You have been unsubscribed successfully.')
    except NewsletterSubscription.DoesNotExist:
        messages.error(request, 'Subscription not found.')

    return redirect('home')
