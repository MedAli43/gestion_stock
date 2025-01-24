from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', ProduitCreateView.as_view(), name='ajouter_produit'),
    path('produits/modifier/<int:pk>/', ProduitUpdateView.as_view(), name='modifier_produit'),
    path('produits/supprimer/<int:pk>/', ProduitDeleteView.as_view(), name='supprimer_produit'),
]