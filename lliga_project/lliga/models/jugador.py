from django.db import models

from .equip import Equip

class Jugador(models.Model):
    nom = models.CharField(max_length=100)
    dorsal = models.IntegerField()
    equip = models.ForeignKey(Equip, on_delete=models.CASCADE)
    posicio = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nom} ({self.dorsal})'
