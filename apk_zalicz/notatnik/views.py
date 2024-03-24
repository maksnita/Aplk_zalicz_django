from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'usun_notatke':
            note_id = request.POST.get('note_id')
            notatka = get_object_or_404(Notatka, id=note_id)
            notatka.delete()
            return redirect('baza')

    przedmioty = Przedmiot.objects.all()
    notatki = Notatka.objects.all()
    return render(request, 'notatnik/baza.html', {'przedmioty': przedmioty, 'notatki': notatki})