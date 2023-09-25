from django.shortcuts import render
from django.shortcuts import redirect


room_info = {
    'single': {
        'name': 'Tek Oda',
        'image_url': '/static/src/images/single1.jpg',
    },
    'classic': {
        'name': 'Klasik Oda',
        'image_url': '/static/src/images/classic1.jpg',
    },
    'superior': {
        'name': 'Superior Oda',
        'image_url': '/static/src/images/superior3.jpg',
    },
    'family-suite': {
        'name': 'Family Suite',
        'image_url': '/static/src/images/family1.jpg',
    },
    'unknown': {
        'name': 'Bilinmeyen Oda',
        'image_url': '/static/src/images/default-room.jpg',
    },
}

def index(request):
    return render(request, 'pages/index-2.html')

def get_room_info(room_type):
    return room_info.get(room_type, room_info['unknown'])

def get_common_context(room_type, room_id):
    room_data = get_room_info(room_type)
    return {
        'room_name': room_data['name'],
        'room_image_url': room_data['image_url'],
        'room_type': room_type,
        'room_id': room_id,
    }

def room_overview(request, room_type):
    room_images = {
        'single': [
            "/static/src/images/single1.jpg",
            "/static/src/images/single2.jpg",
            "/static/src/images/single3.jpg",
        ],
        'classic': [
            "/static/src/images/classic1.jpg",
            "/static/src/images/classic2.jpg",
            "/static/src/images/classic3.jpg",
        ],
        'superior': [
            "/static/src/images/superior3.jpg",
            "/static/src/images/superior2.jpg",
            "/static/src/images/superior1.jpg",
        ],
        'family-suite': [
            "/static/src/images/family1.jpg",
            "/static/src/images/family2.jpg",
            "/static/src/images/family3.jpg",
        ],
    }

    if room_type in room_images:
        room_image_urls = room_images[room_type]
    else:
        room_image_urls = ["/static/src/images/default-room.jpg"]

    context = {
        'room_image_urls': room_image_urls,
        'room_type': room_type,
    }
    return render(request, 'pages/room-overview.html', context)

def room_reservation(request, room_type, room_id):
    context = get_common_context(room_type, room_id)
    return render(request, 'pages/reservation-1.html', context)

def reservation_step_2(request, room_type, room_id):
    context = get_common_context(room_type, room_id)
    return render(request, 'pages/reservation-2.html', context)

def reservation_step_3(request, room_type, room_id):
    context = get_common_context(room_type, room_id)
    return render(request, 'pages/reservation-3.html', context)