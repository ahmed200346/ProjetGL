from users.models import User
from django.db import models
class Artistes(User):
    is_artist=True
    def __str__(self):
        return f"Artiste: {self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "Artiste"
        verbose_name_plural = "Artiste"