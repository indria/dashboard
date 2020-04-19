from django import forms
from django.forms import ModelForm
from dashboard.subs.models import Subscription


class SubscriptionForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    labels = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Subscription
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():            
            self.fields[field].widget.attrs.update({'class': 'form-control'})
 