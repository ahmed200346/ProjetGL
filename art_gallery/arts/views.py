from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView ,DeleteView,DetailView
from .models import *
class ArtistView(ListView):
    model = Art
    template_name = 'index.html'
    context_object_name = 'arts'
    def get_queryset(self):        
        abo = self.request.user.id  # Access request via self
        return Art.objects.filter(owner=abo)
    
class DetailsArtView(DetailView):
    model=Art
    template_name="art_details.html"
    context_object_name = 'art'
class DeleteArtView(DeleteView):
    model=Art
    template_name="index.html"
    success_url=reverse_lazy("list_arts")