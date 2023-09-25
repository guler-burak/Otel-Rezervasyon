from django.shortcuts import render

def index(request):
    return render(request, 'pages/index-2.html')

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
            "/static/src/images/superior-room3.jpg",
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
