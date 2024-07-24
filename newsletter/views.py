# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import SubscriptionInfo, NewsletterSubscription

def subscribe_view(request):
    # Fetch the subscription info; adjust the filter as needed
    subscription_info = get_object_or_404(SubscriptionInfo, id=1)
    user = request.user if request.user.is_authenticated else None
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            if user:
                subscription.user = user
            subscription.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')  # Redirect to home or another page
        else:
            messages.error(request, 'There was an error with your subscription.')
    else:
        form = SubscriptionForm()

    if user:
        existing_subscription = NewsletterSubscription.objects.filter(user=user).first()
        if existing_subscription:
            messages.info(request, 'You are already subscribed to the newsletter.')

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
        subscription.delete()
        messages.success(request, 'You have been unsubscribed successfully.')
    except NewsletterSubscription.DoesNotExist:
        messages.error(request, 'Subscription not found.')

    return redirect('home')