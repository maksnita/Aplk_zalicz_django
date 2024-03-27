"""
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Maksymilian Nita
Data wykonania zadania: 25.03.2024r.
Treść zadania: Aplikacja do prowadzenia notatek z lekcji.
Opis funkcjonalności aplikacji: Aplikacja oferuje funkcjonalność zapisu, przeglądania, edycji i usunięcia notatki oraz filtrację według przedmiotu.
    Oferuje również dodawanie i usuwanie własnych przedmiotów szkolnych.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notatnik.urls')),
]
