from django.http import Http404
from django.shortcuts import render
from dashboard.subs.models import Subscription
from dashboard.subs.forms import SubscriptionForm


def subscriptions(request):
    payload = {}
    if request.user:
        payload.update(subscrptions = Subscription.objects.filter(user = request.user))
        return render(request, 'subs/subs.html', payload)
    
    
def addSub(request):
    payload = {}
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
    else:
        form = SubscriptionForm()
        
    payload.update(form = form )
    return render(request, 'subs/addSub.html', payload)