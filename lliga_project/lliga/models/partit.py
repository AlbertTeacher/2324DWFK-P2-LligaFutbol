from django.db import models

from .equip import Equip
from .lliga import Lliga

class Partit(models.Model):
    lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)
    equip_local = models.ForeignKey(Equip, related_name='partits_local', on_delete=models.CASCADE)
    equip_visitant = models.ForeignKey(Equip, related_name='partits_visitant', on_delete=models.CASCADE)
    data = models.DateTimeField()
    
    def resultat(self):
        gols_local = self.event_set.filter(tipus='GOL', jugador__equip=self.equip_local).count()
        gols_visitant = self.event_set.filter(tipus='GOL', jugador__equip=self.equip_visitant).count()
        return f"{gols_local} - {gols_visitant}"

    def __str__(self):
        return f'{self.equip_local.nom} vs {self.equip_visitant.nom} ({self.data.strftime("%d/%m/%Y %H:%M")})'
