from django.contrib import admin

from .event_inline import EventInline

from ..models import Partit


class PartitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["equip_local", "equip_visitant", "data"]}),
        
    ]
    inlines = [EventInline,]

admin.site.register(Partit, PartitAdmin)
