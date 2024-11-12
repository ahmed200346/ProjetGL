from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Art

class ArtCreateView(CreateView):
    model = Art
    fields = ['title','price','owner_name', 'type', 'categorie', 'description', 'tags', 'fichier']
    template_name = 'prjetse/art_create.html'  
    success_url = reverse_lazy('art_list')
class ArtListView(ListView):
    model = Art
    template_name = 'prjetse/art_list.html'
    context_object_name = 'arts'
class ArtUpdateView(UpdateView):
    model = Art
    fields = ['title','price','owner_name', 'type', 'categorie', 'description', 'tags', 'fichier']
    template_name = 'prjetse/art_update.html'
    success_url = reverse_lazy('art_list')
class ArtDeleteView(DeleteView):
    model = Art
    template_name = 'prjetse/art_confirm_delete.html'
    success_url = reverse_lazy('art_list')
