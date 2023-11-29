from django.contrib import admin
from .models import Contact
from .models import Room, Customer, Reservation

class RoomAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ReservationAdmin(admin.ModelAdmin):
    autocomplete_fields = ["room"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'subject']
    search_fields = ['name', 'surname', 'email', 'subject']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad', 'soyad', 'telefon')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'telefon']
    search_fields = ['first_name', 'last_name', 'email', 'telefon']
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)