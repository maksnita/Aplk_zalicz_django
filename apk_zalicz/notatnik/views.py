from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils import timezone

def notatnik(request):
    form = NotatkaForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'nowy_przedmiot':
            nazwa_nowego_przedmiotu = request.POST.get('new-subject')
            Przedmiot.objects.create(nazwa=nazwa_nowego_przedmiotu)
            przedmioty = Przedmiot.objects.all()
            return render(request, 'notatnik/notatnik.html', {'przedmioty': przedmioty})
        elif action == 'zapisz_notatke':
            form = NotatkaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('baza')

    przedmioty = Przedmiot.objects.all()
    return render(request, 'notatnik/notatnik.html', {'form': form, 'przedmioty': przedmioty})

def baza(request):
    przedmioty = Przedmiot.objects.all()
    notatki = Notatka.objects.all()
    return render(request, 'notatnik/baza.html', {'przedmioty': przedmioty, 'notatki': notatki})