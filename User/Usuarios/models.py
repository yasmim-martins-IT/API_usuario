from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.contrib.auth.models import AbstractUser

class UserAbs(AbstractUser):
    biografia = models.CharField(max_length=200)
    idade = models.IntegerField( validators=[MaxValueValidator(110) , MinValueValidator(0)])
    telefone = models.IntegerField(default=0)
    escolaridade = models.CharField(max_length=100)
    animais = models.IntegerField(default=0)
    endereco = models.CharField(max_length=255, default="Endereço não informado")


    def __str__(self):
        return self.username

# Create your models here.
