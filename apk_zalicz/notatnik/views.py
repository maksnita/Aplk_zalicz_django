"""
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Maksymilian Nita
Data wykonania zadania: 25.03.2024r.
Treść zadania: Aplikacja do prowadzenia notatek z lekcji.
Opis funkcjonalności aplikacji: Aplikacja oferuje funkcjonalność zapisu, przeglądania, edycji i usunięcia notatki oraz filtrację według przedmiotu.
    Oferuje również dodawanie i usuwanie własnych przedmiotów szkolnych.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Funkcja obsługi widoku strony notatnik.html
def notatnik(request):
    form = NotatkaForm()

    try:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'nowy_przedmiot':
                przedmioty = Przedmiot.objects.all()
                nazwa_nowego_przedmiotu = request.POST.get('new-subject')

                if Przedmiot.objects.filter(nazwa=nazwa_nowego_przedmiotu).exists():
                    error_message = 'Przedmiot o tej nazwie już istnieje!'
                    return render(request, 'notatnik/notatnik.html', {'error_message': error_message, 'przedmioty': przedmioty})
                else:
                    Przedmiot.objects.create(nazwa=nazwa_nowego_przedmiotu)
                    message = 'Przedmiot został pomyślnie dodany!'
                    return render(request, 'notatnik/notatnik.html', {'message': message, 'przedmioty': przedmioty})
            elif action == 'usun_przedmiot':
                przedmiot_id = request.POST.get('przedmiot_usun')
                przedmiot = get_object_or_404(Przedmiot, id=przedmiot_id)
                przedmiot.delete()
                przedmioty = Przedmiot.objects.all()
                message = 'Przedmiot został pomyślnie usunięty!'
                return render(request, 'notatnik/notatnik.html', {'message': message, 'przedmioty': przedmioty})
            elif action == 'zapisz_notatke':
                form = NotatkaForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('baza')
    except Exception as e:
        error_message = str(e)
        przedmioty = Przedmiot.objects.all()
        return render(request, 'notatnik/notatnik.html', {'error_message': error_message, 'przedmioty': przedmioty})

    przedmioty = Przedmiot.objects.all()
    return render(request, 'notatnik/notatnik.html', {'form': form, 'przedmioty': przedmioty})

# Funkcja obsługi widoku strony baza.html
def baza(request):

    try:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'usun_notatke':
                note_id = request.POST.get('note_id')
                notatka = get_object_or_404(Notatka, id=note_id)
                notatka.delete()
                message_del = "Notatka została pomyślnie usunięta!"
                przedmioty = Przedmiot.objects.all()
                notatki = Notatka.objects.order_by('-data_utworzenia')
                return render(request, 'notatnik/baza.html', {'przedmioty': przedmioty, 'notatki': notatki, 'message_del': message_del})
            elif action == 'edytuj_notatke':
                note_id = request.POST.get('note_id')
                edited_content = request.POST.get('edited_content')
                notatka = get_object_or_404(Notatka, id=note_id)
                notatka.tresc = edited_content
                notatka.save()
                return redirect('baza')
    except Exception as e:
        error_message = str(e)
        przedmioty = Przedmiot.objects.all()
        return render(request, 'notatnik/notatnik.html', {'error_message': error_message, 'przedmioty': przedmioty})


    przedmioty = Przedmiot.objects.all()
    notatki = Notatka.objects.order_by('-data_utworzenia')
    return render(request, 'notatnik/baza.html', {'przedmioty': przedmioty, 'notatki': notatki})