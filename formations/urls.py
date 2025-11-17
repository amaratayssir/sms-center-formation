from django.urls import path
from . import views  # Importe tes vues

urlpatterns = [
    path('', views.catalogue, name='catalogue'),  # /formations/ → liste
    path('', views.accueil, name='accueil'),  # / → accueil
    path('inscription/', views.inscription_view, name='inscription'),
]