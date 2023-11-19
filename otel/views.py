from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from .models import Room, Contact
from .forms import ContactForm, RegisterForm, LoginForm
from django.contrib import messages

def index(request):
    rooms = Room.objects.all()
    return render(request, 'pages/index.html', {'rooms': rooms})

def about(request):
    return render(request, 'pages/about.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hesap başarıyla oluşturuldu. Şimdi giriş yapabilirsiniz.')
            return redirect('index')
        else:
            messages.error(request, 'Lütfen formu doğru bir şekilde doldurun.') 
    else:
        form = RegisterForm()

    return render(request, 'pages/register.html', {'form': form}) 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            if user := authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password']):
                login(request, user)
                messages.success(request, 'Başarıyla giriş yaptınız.')
                return redirect('index')
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'login_form': form})

def category(request):
    return render(request, 'pages/rooms-category.html')

def facility(request):
    return render(request, 'pages/facility.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Her zaman yeni bir kayıt oluştur
            Contact.objects.create(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Mesajınız başarıyla gönderildi.')
            return redirect('index')  # Başarı sayfasına yönlendirme
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

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

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hesap başarıyla oluşturuldu. Şimdi giriş yapabilirsiniz.')
            return redirect('login')
        else:
            messages.error(request, 'Lütfen formu doğru bir şekilde doldurun.')
    else:
        form = RegisterForm()

    context = {'room': room, 'form': form}
    return render(request, 'pages/reservation-2.html', context)

def reservation_step_3(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    context = {'room': room}
    return render(request, 'pages/reservation-3.html', context)

