from django.shortcuts import render
from .models import Resources


def travel_resources(request):
    """
    Renders the resources page
    """
    resources = Resources.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "resources/resources.html",
        {"resources": resources},
    )