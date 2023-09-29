from django.db import models
import segno
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class QRCODE(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Dê um apelido para este código")
    url = models.CharField(max_length=100, help_text="Para onde este QRCODE leva")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qrcode_img = models.ImageField(upload_to="qrcode_images")
    public = models.BooleanField(default=True)
