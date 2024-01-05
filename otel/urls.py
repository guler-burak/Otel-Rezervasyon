from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, user_logout, success
from .views import complete_reservation


urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
    path('tesisler/', views.facility, name='facility'),
    path('room-category/', views.category, name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success, name='success'),
    path('success2/', views.success2, name='success2'),
    path('logout/', user_logout, name='logout'),
    path('reservation/<slug:room_slug>/step-3/', views.reservation_step_3, name='reservation-step-3'),
    path('reservation/<slug:room_slug>/step-2/', views.reservation_step_2, name='reservation-step-2'),
    path('reservation/<slug:room_slug>/', views.reservation, name='reservation'),
    path('<slug:room_slug>/', views.room_overview, name='room-overview'),
    path('complete_reservation/<slug:room_slug>/', complete_reservation, name='complete_reservation'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
