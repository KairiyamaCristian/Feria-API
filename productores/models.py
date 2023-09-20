from django.db import models
from shared.models import User


# Create your models here.
class Productor(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    dni = models.IntegerField(default=0, null=True)
    domicilio = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return super().__str__()
