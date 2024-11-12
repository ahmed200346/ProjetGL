from django.db import models

# Create your models here.
import re
from django.core.exceptions import ValidationError
from django.db import models
import os
#from paiement import Paiement
from enum import Enum
from django.apps import apps


# Définition de l'énumération pour le type d'art
class ArtType(Enum):
    IMAGE = 'Image'
    VIDEO = 'Vidéo'
    MUSIQUE = 'Musique'



# Validation de type de fichier
def validate_art_file_type(value):
    # Récupérer le type d'art depuis l'instance du modèle (ne peut pas être dans un validateur de champ)
    art_type = ArtType[value.instance.type]  # Accéder à l'objet enum correspondant à la chaîne
    filename = value.name  # Nom du fichier
    
    # Dictionnaire des types de fichiers autorisés selon le type d'art
    allowed_file_types = {
        ArtType.IMAGE: ['.png', '.jpg', '.jpeg', '.gif','jfif'],
        ArtType.VIDEO: ['.mp4', '.avi', '.mov'],
        ArtType.MUSIQUE: ['.mp3', '.wav']
    }
    
    # Utilisation de os.path.splitext pour obtenir l'extension en minuscules
    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()  # Assure que l'extension est en minuscules
    
    if not any(file_extension == ext for ext in allowed_file_types.get(art_type, [])):
        raise ValidationError(f"Le fichier '{filename}' n'est pas autorisé pour le type '{art_type.value}'.")


def validate_max_size(value):
    max_size = 10 * 1024 * 1024  # 10MB
    if value.size > max_size:
        raise ValidationError("Le fichier est trop volumineux. La taille maximale est de 10 Mo.")


class Art(models.Model):
    ID_art = models.AutoField(primary_key=True)  # Clé primaire
    title=models.CharField(max_length=50,default='art')
    owner_name = models.CharField(max_length=50) 
    type = models.CharField(
        max_length=50,
        choices=[(art_type.name, art_type.value) for art_type in ArtType]  # Utilisation des choix d'Enum
    )
    categorie = models.CharField(max_length=50)  # Catégorie de l'art
    description = models.TextField()  # Description de l'art
    tags = models.CharField(max_length=200, blank=True)  # Tags associés
    paiement = models.ForeignKey('paiement.Paiement', on_delete=models.CASCADE, related_name='arts', blank=True, null=True)
    fichier = models.FileField(upload_to='prjetse/', default='path/to/default/file', validators=[validate_art_file_type, validate_max_size])
    price = models.FloatField()


    def save(self, *args, **kwargs):
        # On utilise la méthode save sans appeler clean() explicitement ici
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.ID_art} - {self.title} ({self.type}) - {self.owner_name}"
