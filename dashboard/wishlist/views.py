from django.http import Http404
from django.shortcuts import render
from dashboard.subs.models import Subscription
from dashboard.subs.forms import SubscriptionForm


def wishlist(request):
    payload = {}
    return render(request, 'wishlist/wishlist.html', payload)