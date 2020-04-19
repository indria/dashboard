from django.contrib import admin
from dashboard.subs.models import Subscription
from dashboard.dash.models import Label

admin.site.register(Subscription)
admin.site.register(Label)