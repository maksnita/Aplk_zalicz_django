from django import forms
from .models import Notatka

class NotatkaForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ['przedmiot', 'tytul', 'tresc']
