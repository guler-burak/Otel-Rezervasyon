from django.shortcuts import render,get_object_or_404, redirect
from django.conf import settings
from .models import Room

def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'pages/index-2.html', context)

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def category(request):
    return render(request, 'pages/rooms-category.html')

def facility(request):
    return render(request, 'pages/facility.html')

def contact(request):
    return render(request, 'pages/contact.html')

def get_room_info(room_type):
    return settings.ROOM_INFO.get(room_type, settings.ROOM_INFO['unknown'])

def get_common_context(room_type, room_id):
    room_data = get_room_info(room_type)
    return {
        'room_name': room_data['name'],
        'room_image_url': room_data['image_url'],
        'room_type': room_type,
        'room_id': room_id,
    }

def room_overview(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    context = {'room': room}
    return render(request, 'pages/room-overview.html', context)

def reservation(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    context = {'room': room}
    return render(request, 'pages/reservation-1.html', context)

def reservation_step_2(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    context = {'room': room}
    return render(request, 'pages/reservation-2.html', context)

def reservation_step_3(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    context = {'room': room}
    return render(request, 'pages/reservation-3.html', context)

