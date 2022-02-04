from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('Flat_town', 'Flat_address', 'Flat_owner')
    readonly_fields = ('created_at',)
