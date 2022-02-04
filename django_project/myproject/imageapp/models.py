from django.db import models

class ImageContent(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="uploads")


class AudioContent(models.Model):
    mp3 = models.FileField(blank=True, null=True, upload_to="uploads")