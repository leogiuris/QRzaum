from django.db import models
from accounts.models import User
import segno


class QRCODE(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Dê um apelido para este código")
    url = models.CharField(max_length=100, help_text="Para onde este QRCODE leva")
    data = models.CharField(max_length=9999,default="none")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_file = models.ImageField(upload_to="files/qrcode_images")
    public = models.BooleanField(default=True)