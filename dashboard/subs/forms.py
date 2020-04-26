from django import forms
from django.conf import settings
from django.forms import ModelForm
from dashboard.dash.models import PeriodChoice
from dashboard.dash.models import PaymentChoice
from dashboard.subs.models import Subscription



class SubscriptionForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    
    class Meta:
        model = Subscription
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():            
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    
    def clean(self):
        self.recurring_unit = str(self.cleaned_data['recurring_unit'])
        self.payment_method = str(self.cleaned_data['payment_method'])
