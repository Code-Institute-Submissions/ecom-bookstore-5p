from django import forms
from django_countries.fields import CountryField

class OrderForm(forms.Form):
    order_id = forms.IntegerField(widget=forms.HiddenInput())
    first_name = forms.CharField(max_length=30, required=False)
    second_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)
    country = forms.CharField(required=False)
    postcode = forms.CharField(max_length=10, required=False)
    address_line_one = forms.CharField(max_length=200, required=False)
    town_city = forms.CharField(max_length=200, required=False)
