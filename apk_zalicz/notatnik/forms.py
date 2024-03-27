"""
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Maksymilian Nita
Data wykonania zadania: 25.03.2024r.
Treść zadania: Aplikacja do prowadzenia notatek z lekcji.
Opis funkcjonalności aplikacji: Aplikacja oferuje funkcjonalność zapisu, przeglądania, edycji i usunięcia notatki oraz filtrację według przedmiotu.
    Oferuje również dodawanie i usuwanie własnych przedmiotów szkolnych.
"""

from django import forms
from .models import Notatka

# Klasa definiująca formularz Django, który pozwala użytkownikom wprowadzać dane dotyczące notatek
class NotatkaForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ['przedmiot', 'tytul', 'tresc']
