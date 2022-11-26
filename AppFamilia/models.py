from django.db import models

# Create your models here.

class Familia(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Edad=models.IntegerField()
