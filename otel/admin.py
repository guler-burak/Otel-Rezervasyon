from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ReservationAdmin(admin.ModelAdmin):
    autocomplete_fields = ["room"]

admin.site.register(Room, RoomAdmin)
