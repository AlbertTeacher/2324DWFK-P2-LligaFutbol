from django.contrib import admin

from ..models import Event

class EventInline(admin.TabularInline):
    model = Event
    # (equip local + visitant), tipus, equip, jugador i temps
    fields = ("tipus", "jugador", "minut")

