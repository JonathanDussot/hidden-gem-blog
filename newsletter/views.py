from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import SubscriptionInfo

def subscribe_view(request):
    # Fetch the subscription info; adjust the filter as needed
    subscription_info = get_object_or_404(SubscriptionInfo, id=1)
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')  # Redirect to home or another page
        else:
            messages.error(request, 'There was an error with your subscription.')
    else:
        form = SubscriptionForm()
    
    return render(
        request,
        'newsletter/subscribe.html',
        {
            'SubscriptionInfo': subscription_info,
            'subscription_form': form 
        }
    )
