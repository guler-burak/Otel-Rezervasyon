from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number','room_type','price']

    class Meta:
        model = Room

admin.site.register(Room,RoomAdmin)