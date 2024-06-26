from django.contrib import admin

from ..models import Equip

class EquipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Equip)
