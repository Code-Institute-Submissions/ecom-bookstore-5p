from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import books.models as bkm

class BookForm(forms.ModelForm):
    class Meta:
        model = bkm.Book
        fields = '__all__'

