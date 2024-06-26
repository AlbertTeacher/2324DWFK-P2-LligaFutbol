from django.contrib import admin

from ..models import Lliga


class LligaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lliga)
