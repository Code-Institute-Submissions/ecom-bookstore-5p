from django import forms
from django_countries.fields import CountryField

class OrderForm(forms.Form):
    order_id = forms.IntegerField(widget=forms.HiddenInput())
    first_name = forms.CharField(max_length=30, required=True)
    second_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    country = forms.CharField(required=True)
    postcode = forms.CharField(max_length=10, required=True)
    address_line_one = forms.CharField(max_length=200, required=True)
    town_city = forms.CharField(max_length=200, required=True)
