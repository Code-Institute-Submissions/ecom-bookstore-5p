from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import books.models as bkm

class SearchForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    genre = forms.ModelChoiceField(
        queryset=bkm.Genre.objects.all().order_by('id')
    )
    author = forms.CharField(max_length=100, required=False)
