from django.db import models
from autoslug import AutoSlugField

class Room(models.Model):
    ROOM_TYPES = (
    ('tek-kisilik', 'Tek Kişilik'),
    ('çift-aile', 'Çift Kişilik'),
    ('suit', 'Süit'),
    ('standart', 'Standart'),
    ('deluxe', 'Deluxe'),
)

    room_type = models.CharField(max_length=100, choices=ROOM_TYPES)
    price = models.PositiveIntegerField()
    room_number = models.CharField(max_length=10, unique=True)
    image_home = models.ImageField(upload_to='room_images/home/')
    image_detail_1 = models.ImageField(upload_to='room_images/detail/')
    image_detail_2 = models.ImageField(upload_to='room_images/detail/')
    image_detail_3 = models.ImageField(upload_to='room_images/detail/')
    description = models.TextField()
    slug = AutoSlugField(populate_from='room_type', unique=True)
