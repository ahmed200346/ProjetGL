from django.contrib import admin

# Register your models here.


from .models import Art

# Classe d'administration personnalisée pour le modèle Art
class ArtAdmin(admin.ModelAdmin):
    # Définir les colonnes qui s'affichent dans la liste des objets Art
    list_display = ['ID_art', 'title','price','owner_name', 'type', 'categorie', 'description', 'tags', 'paiement', 'fichier']
    
    # Permettre à l'admin de filtrer les objets Art par type ou catégorie
    list_filter = ['type', 'categorie']
    
    # Permettre à l'admin de rechercher par référence, nom du propriétaire et catégorie
    search_fields = ['title', 'owner_name', 'categorie']
    
    # Définir l'ordre d'affichage des objets
    ordering = ['ID_art']
    
    # Permettre de sélectionner des actions en masse (par exemple, suppression en masse)
    actions = ['delete_selected']

    # Personnaliser la vue d'ajout ou de modification d'un Art
    fieldsets = (
        (None, {
            'fields': ('title','price','owner_name', 'type', 'categorie', 'description', 'tags', 'fichier', 'paiement')
        }),
    )
    
    # Exclure certains champs lors de la création d'un nouvel Art (si nécessaire)
    # exclude = ['ID_art'] # On peut exclure certains champs, comme l'ID, s'il est automatique.

    # Permettre l'édition en ligne des objets Art dans les relations, si besoin
    # inlines = [PaiementInline]

# Enregistrer le modèle Art et sa configuration d'admin
admin.site.register(Art, ArtAdmin)


