from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    Phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profiles', default='user.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)