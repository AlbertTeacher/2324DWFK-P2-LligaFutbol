from django.db import models

from .lliga import Lliga

class Equip(models.Model):
    nom = models.CharField(max_length=100)
    lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)
    ciutat = models.CharField(max_length=100)
    estadi = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
