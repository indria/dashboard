from django.db import models
from enum import Enum


class PeriodChoice(Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"
    
    def __str__(self):
        return str(self.value)


class PaymentChoice(Enum):
    CASH = "Cash"
    CC = "Credit Card"
    
    def __str__(self):
        return str(self.value)



class Label(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    colour = models.CharField(max_length=6)

    def __str__(self):
        return self.name

 