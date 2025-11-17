from django.shortcuts import render
from .models import Formation  # Importe ton modèle
from django.shortcuts import render, redirect
from django.contrib.auth import login  # Pour auto-login après inscription
from django.contrib import messages  # Pour feedback
from .forms import InscriptionUserForm

def catalogue(request):
    formations = Formation.objects.all()  # Récupère toutes les formations de la DB
    return render(request, 'formations/catalogue.html', {'formations': formations})  # Passe à template
def accueil(request):
    return render(request, 'base.html')  # Utilise base sans block

def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte auto
            messages.success(request, 'Inscription réussie ! Bienvenue.')
            return redirect('catalogue')  # Redirige vers catalogue
    else:
        form = InscriptionUserForm()
    return render(request, 'formations/inscription.html', {'form': form})