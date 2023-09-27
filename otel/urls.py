from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_type>-room/', views.room_overview, name='room-overview'),
    path('<str:room_type>-room/reservation-<int:room_id>/', views.room_reservation, name='room-reservation'),
    path('<str:room_type>-room/reservation-<int:room_id>/reservation-2/', views.reservation_step_2, name='reservation-step-2'),
    path('<str:room_type>-room/reservation-<int:room_id>/reservation-2/reservation-3/', views.reservation_step_3, name='reservation-step-3'), 
    path('about/', views.about, name='about'),
    path('facility/', views.facility, name='facility'),
    path('contact/', views.contact, name='contact'),

]
