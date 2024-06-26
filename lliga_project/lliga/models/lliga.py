from django.db import models

class Lliga(models.Model):
    nom = models.CharField(max_length=100)
    nivell = models.IntegerField()  # Per representar 1a, 2a, 3a divisió

    def __str__(self):
        return self.nom
