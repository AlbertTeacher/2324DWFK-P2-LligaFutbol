from asyncio import Event
from django.contrib import admin

from .models import Lliga, Equip, Jugador, Partit, Event

admin.site.register(Lliga)
admin.site.register(Equip)
admin.site.register(Jugador)
admin.site.register(Partit)
admin.site.register(Event)