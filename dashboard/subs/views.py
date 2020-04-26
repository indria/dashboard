from django.http import Http404
from django.shortcuts import render
from dashboard.subs.models import Subscription
from dashboard.subs.forms import SubscriptionForm


def subscriptions(request):
    payload = {}
    if request.user:
        payload.update(subscrptions = Subscription.objects.all())
        return render(request, 'subs/subs.html', payload)
    
    
def subscription_form(request):
    payload = {}
    form = SubscriptionForm()
    payload.update(form = form )
    return render(request, 'subs/addSub.html', payload)


def add_subscription(request):
    payload = {}
    form = SubscriptionForm(request.POST)
    form.save()
    payload.update(form = SubscriptionForm())
    return render(request, 'subs/addSub.html', payload)