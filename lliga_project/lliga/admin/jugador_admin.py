from django.contrib import admin

from ..models import Jugador


class JugadorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Jugador)