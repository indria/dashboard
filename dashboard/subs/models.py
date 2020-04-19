from django.db import models
from django.contrib.auth.models import User
from dashboard.dash.models import PeriodChoice
from dashboard.dash.models import PaymentChoice
from dashboard.dash.models import Label

class Subscription(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    currency = models.CharField(max_length=3)
    recurring = models.BooleanField()
    start_date = models.DateField()
    recurring_period = models.SmallIntegerField()
    recurring_unit = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in PeriodChoice])
    payment_method = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in PaymentChoice])
    labels = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name