from django import forms
from django_countries.fields import CountryField

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    second_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()
    country = CountryField()
