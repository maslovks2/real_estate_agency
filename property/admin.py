from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("owner",)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('Flat_town', 'Flat_address', 'Flat_owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('users_who_liked',)
    inlines = [
        OwnersInline,
    ]


@admin.register(Complaint)
class ComplatintAdmin(admin.ModelAdmin):
    fields = ("author", "flat", "text")
    raw_id_fields = ("flat", "author")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    list_display = ("name", "owner_pure_phone")
