from django.shortcuts import render
from .models import Organization


def display_organizations(request):
    """
    A view to display the organizations available
    for the user to support
    """
    organizations = Organization.objects.all()

    template = 'organizations/organizations.html'

    context = {
        'organizations': organizations,
    }

    return render(request, template, context)
