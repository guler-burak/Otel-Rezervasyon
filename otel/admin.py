from django.contrib import admin
from .models import Contact
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ReservationAdmin(admin.ModelAdmin):
    autocomplete_fields = ["room"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'subject']
    search_fields = ['name', 'surname', 'email', 'subject']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Room, RoomAdmin)
