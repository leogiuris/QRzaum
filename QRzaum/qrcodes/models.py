from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    email = models.EmailField(help_text='Informe o email', max_length=254)
    
    def __str__(self):
        return self.nome

class QRCODE(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Dê um apelido para este código')
    url = models.CharField(max_length=100, help_text='Para onde este QRCODE leva')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

