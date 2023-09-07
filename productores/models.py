from django.db import models
from shared.models import User


# Create your models here.
class Productor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=512)
