from django import forms
# from django_countries.fields import CountryField
import django_countries as dc
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('payment_intent', 'user',)
