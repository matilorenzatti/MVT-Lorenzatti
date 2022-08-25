from django.db import models


class Familia(models.Model):
    nombre = models.CharField(max_length=50, unique=True,)
    edad = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField(unique=True)
