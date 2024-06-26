from django.contrib import admin

from ..models import Partit


class PartitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partit)
