from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    