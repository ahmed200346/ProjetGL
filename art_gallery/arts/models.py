from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from artistes.models import Artistes

class Art(models.Model):
    id_art = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(Artistes, on_delete=models.CASCADE, related_name='arts') 
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True) 
    tags = models.CharField(max_length=255, blank=True, help_text="Tags séparés par des virgules")
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(
        upload_to='arts/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png', 'mp4', 'mp3'],message="Arts doit etre soit musique .mp3 ou .mp4 soit image :. jpg ou .png soit vidéo .mp4")
        ]
    )
    def __str__(self):
        return f"{self.title} "
    @property
    def tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
