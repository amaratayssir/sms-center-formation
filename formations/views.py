from django.shortcuts import render
from .models import Formation  # Importe ton modèle

def catalogue(request):
    formations = Formation.objects.all()  # Récupère toutes les formations de la DB
    return render(request, 'formations/catalogue.html', {'formations': formations})  # Passe à template