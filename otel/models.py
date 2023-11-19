from django.db import models
from autoslug import AutoSlugField

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