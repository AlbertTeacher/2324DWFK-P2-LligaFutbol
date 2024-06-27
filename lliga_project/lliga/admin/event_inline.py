from django.contrib import admin

from ..models import Event, Jugador, Equip, Partit

class EventInline(admin.TabularInline):
    model = Event
    extra = 0
    # (equip local + visitant), tipus, equip, jugador i temps
    # fields = ("tipus", "jugador", "minut")

