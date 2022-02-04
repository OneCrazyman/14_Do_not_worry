from django.db import models

class SwiperContent(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="uploads")
    mp3 = models.FileField(blank=True, null=True, upload_to="uploads")