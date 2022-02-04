from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('Flat_town', 'Flat_address', 'Flat_owner')


admin.site.register(Flat, FlatAdmin)
