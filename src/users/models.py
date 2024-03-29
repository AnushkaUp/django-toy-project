from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Account"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        picture = Image.open(self.image.path)

        if picture.height > 300 or picture.width > 300:
            new_size = (300, 300)
            picture.thumbnail(new_size)
            picture.save(self.image.path)
