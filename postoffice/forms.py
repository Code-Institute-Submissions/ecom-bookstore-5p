from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewsletterForm(forms.Form):
    subject = forms.CharField(min_length=3, max_length=200)
    body = forms.CharField(min_length=5, max_length=2000)

