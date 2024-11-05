from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re
def only_Letters(value):
    if not re.match(r'^[a-zA-Z]+$', value):
        raise ValidationError('Ce champ ne doit contenir que des lettres.')
def Email_Valide(value):
    liste=["@gmail.com","@esprit.tn"]
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=30, validators=[only_Letters])
    last_name = models.CharField(max_length=30, validators=[only_Letters])
    email = models.EmailField(unique=True)
    username= models.CharField(max_length=50, unique=True)
    USERNAME_FIELD="username"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
