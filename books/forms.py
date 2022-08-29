from django import forms
from django.core.exceptions import ValidationError
import books.models as bkm


class SearchForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    genre = forms.ModelChoiceField(
        queryset=bkm.Genre.objects.all().order_by('id'),
        required=False
    )
    author = forms.CharField(max_length=100, required=False)
