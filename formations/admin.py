from django.contrib import admin
from .models import Formation, Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']  # Colonne visible en admin

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'duree', 'prix', 'date_creation']  # Vue liste
    list_filter = ['categorie', 'date_creation']  # Filtres
    search_fields = ['titre', 'description']  # Recherche