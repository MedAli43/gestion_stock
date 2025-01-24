from django.shortcuts import render
from .models import Produit
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

class ProduitCreateView(CreateView):
    model = Produit
    fields = ['nom', 'description', 'prix', 'quantite', 'categorie']  # Fields to include in the form
    template_name = 'stock/produit_form.html'  # Template for the form
    success_url = reverse_lazy('liste_produits')  # Redirect after successful submission

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'stock/liste_produits.html', {'produits': produits})

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = ['nom', 'description', 'prix', 'quantite', 'categorie']  # Fields to include in the form
    template_name = 'stock/produit_form.html'  # Reuse the same template as for creating
    success_url = reverse_lazy('liste_produits')  # Redirect after successful update

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'stock/produit_confirm_delete.html'  # Template for the confirmation page
    success_url = reverse_lazy('liste_produits')  # Redirect after successful deletion