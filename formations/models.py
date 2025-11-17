from django.db import models
from django.contrib.auth.models import User  # Pour formateur

class Categorie(models.Model):
    nom = models.CharField(max_length=50)  # ex. 'Informatique'
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    duree = models.IntegerField(help_text="En heures")  # ex. 20
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # ex. 200.00
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    formateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Inscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur inscrit
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)  # Formation choisie
    date_inscription = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20, 
        choices=[('en_attente', 'En attente'), ('payee', 'Payée'), ('annulee', 'Annulée')],
        default='en_attente'
    )
    # Plus tard : champ pour session_date ou paiement_id

    def __str__(self):
        return f"Inscription de {self.user.username} à {self.formation.titre}"
    def __str__(self):
        return f"{self.titre} ({self.categorie.nom})"
    