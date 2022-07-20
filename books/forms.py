from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import books.models as bkm

class SearchForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    genre = forms.ModelChoiceField(
        queryset=bkm.Genre.objects.all().order_by('id'),
        required=False
    )
    author = forms.CharField(max_length=100, required=False)

    # https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model.clean
    def clean(self):
        a = not bool(self.cleaned_data['name'])
        b = not bool(self.cleaned_data['author'])
        c = not bool(self.cleaned_data['genre'])

        if a and b and c:
            raise ValidationError('Atleast One Input Must Be Filled')
