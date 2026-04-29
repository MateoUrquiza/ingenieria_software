from django.db import models

# Create your models here.

class Proveedor():
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=10)
    correo = models.CharField(max_length=50)


class Producto(models.Model):
    
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

    