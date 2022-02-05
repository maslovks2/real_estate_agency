from csv import list_dialects
from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('Flat_town', 'Flat_address', 'Flat_owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


@admin.register(Complaint)
class ComplatintAdmin(admin.ModelAdmin):
    fields = ("user", "flat", "text")
    raw_id_fields = ("flat", "user")
