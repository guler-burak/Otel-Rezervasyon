from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_type>-room/', views.room_overview, name='room-overview'),
]
