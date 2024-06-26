from django.db import models

from .jugador import Jugador
from .partit import Partit

class Event(models.Model):
    TIPUS_EVENT = [
        ('GOL', 'Gol'),
        ('TG', 'Targeta Groga'),
        ('TV', 'Targeta Vermella'),
        ('FALTA', 'Falta'),
        # Afegiu més tipus d'esdeveniments si cal
    ]

    partit = models.ForeignKey(Partit, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    tipus = models.CharField(max_length=5, choices=TIPUS_EVENT)
    minut = models.IntegerField()
    descripcio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.partit} - {self.jugador.nom} ({self.tipus}) al minut {self.minut}'
