from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Room, Contact, Reservation  
from .forms import ContactForm, RegisterForm, LoginForm
from django.contrib import messages
from .forms import ReservationForm, Customer
from datetime import datetime

def index(request):
    rooms = Room.objects.all()
    return render(request, 'pages/index.html', {'rooms': rooms})

def about(request):
    return render(request, 'pages/about.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['ad']
            user.last_name = form.cleaned_data['soyad']
            user.save()

            Customer.objects.create(user=user, ad=form.cleaned_data['ad'],
                                    soyad=form.cleaned_data['soyad'],
                                    telefon=form.cleaned_data['telefon'])
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
                return redirect('index')
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'login_form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

def category(request):
    return render(request, 'pages/rooms-category.html')

def facility(request):
    return render(request, 'pages/facility.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Mesajınız başarıyla gönderildi.')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

def calculate_price(start_date, end_date, daily_rate):
    num_days = (end_date - start_date).days + 1
    total_price = num_days * daily_rate
    return total_price

def room_overview(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    context = {'room': room}

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        form.room = room
        if form.is_valid():
            return render(request, 'pages/reservation-1.html', context)

    else:
        form = ReservationForm()
        form.room = room

    context['form'] = form
    return render(request, 'pages/room-overview.html', context)


def reservation(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            checkin_date = form.cleaned_data['checkin_date']
            checkout_date = form.cleaned_data['checkout_date']

            num_days = (checkout_date - checkin_date).days + 1
            total_price = num_days * room.price

            request.session['checkin_date'] = checkin_date.strftime("%Y-%m-%d")
            request.session['checkout_date'] = checkout_date.strftime("%Y-%m-%d")
            request.session['total_price'] = total_price

            return render(request, 'pages/reservation-1.html', {'room': room, 'checkin_date': checkin_date, 'checkout_date': checkout_date, 'total_price': total_price})

    else:
        form = ReservationForm()

    return render(request, 'pages/reservation-1.html', {'room': room, 'form': form})

def reservation_step_2(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)

    checkin_date_str = request.session.get('checkin_date')
    checkout_date_str = request.session.get('checkout_date')

    checkin_date = datetime.strptime(checkin_date_str, "%Y-%m-%d") if checkin_date_str else None
    checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d") if checkout_date_str else None

    total_price = 0
    if checkin_date and checkout_date:
        total_price = calculate_price(checkin_date, checkout_date, room.price)

    return render(request, 'pages/reservation-2.html', {'room': room, 'checkin_date': checkin_date, 'checkout_date': checkout_date, 'total_price': total_price})

def reservation_step_3(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)

    checkin_date_str = request.session.get('checkin_date')
    checkout_date_str = request.session.get('checkout_date')

    checkin_date = datetime.strptime(checkin_date_str, "%Y-%m-%d") if checkin_date_str else None
    checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d") if checkout_date_str else None

    total_price = 0
    if checkin_date and checkout_date:
        total_price = calculate_price(checkin_date, checkout_date, room.price)

    return render(request, 'pages/reservation-3.html', {'room': room, 'checkin_date': checkin_date, 'checkout_date': checkout_date, 'total_price': total_price})

def complete_reservation(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)

    if request.method == 'POST':
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        telefon = request.user.customer.telefon

        checkin_date = request.session.get('checkin_date')
        checkout_date = request.session.get('checkout_date')

        reservation = Reservation(
            first_name=first_name,
            last_name=last_name,
            email=email,
            telefon=telefon,
            name=room.name, 
            checkin_date=checkin_date,
            checkout_date=checkout_date
        )
        reservation.save()
        return redirect('index')

    return render(request, 'pages/reservation-3.html', {'room': room})