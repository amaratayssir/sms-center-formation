from django.urls import path
from . import views  # Importe tes vues

urlpatterns = [
    path('', views.catalogue, name='catalogue'),  # /formations/ → liste
]