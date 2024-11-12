

# Create your models here.
from django.db import models

class Paiement(models.Model):
    ID_vente = models.AutoField(primary_key=True)
    date_paiement = models.DateField()
    prix_paiement = models.DecimalField(max_digits=10, decimal_places=2)

    def ajouter(self):
        pass

    def modifier(self):
        pass

    def annuler(self):
        pass

    def __str__(self):
        return f"Paiement {self.ID_vente} - Date: {self.date_paiement} - Prix: {self.prix_paiement} €"
