from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ad")
    price = models.PositiveIntegerField()
    image_home = models.ImageField(upload_to='room_images/home/')
    image_detail_1 = models.ImageField(upload_to='room_images/detail/')
    image_detail_2 = models.ImageField(upload_to='room_images/detail/')
    image_detail_3 = models.ImageField(upload_to='room_images/detail/')
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = "Oda"
        verbose_name_plural = "Odalar"

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"
    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ad = models.CharField(max_length=30, blank=True)
    soyad = models.CharField(max_length=30, blank=True)
    telefon = models.CharField(max_length=15, blank=True)
    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    telefon = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"