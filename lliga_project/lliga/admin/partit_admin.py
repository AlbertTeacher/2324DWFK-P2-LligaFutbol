from django.contrib import admin

from .event_inline import EventInline

from ..models import Partit, Event


@admin.register(Partit)
class PartitAdmin(admin.ModelAdmin):
    readonly_fields = ['ro_resultat',]
    fields = ['equip_local', 'equip_visitant', 'lliga', 'data', 'ro_resultat']
    list_display = ['equip_local', 'equip_visitant', 'lliga', 'data', 'resultat']
    inlines = [EventInline,]

    @admin.display(description='Resultat')
    def ro_resultat(self, instance):
        res = instance.resultat()
        return res
