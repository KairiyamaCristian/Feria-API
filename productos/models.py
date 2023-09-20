from django.db import models
from categorias.models import Categoria

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precioXUnidad = models.FloatField(default=0)
    precioXKg = models.FloatField(default=0)
    descripcion = models.CharField(max_length=50)
    organico = models.BooleanField()
    f_almacenamiento = models.DateField(auto_now_add=True)
    destacado = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
