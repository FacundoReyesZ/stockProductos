from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.nombre
