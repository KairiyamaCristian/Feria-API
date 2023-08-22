from django.db import models


# Create your models here.
class Productor(models.Model):
    nombre = models.TextField(max_length=500)
    apellido = models.TextField(max_length=500)
