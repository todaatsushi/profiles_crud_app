"""
Home page view.

Redirects to user list view in the users app.
"""
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect(reverse('user-list'))
