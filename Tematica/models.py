from django.db import models

class Proveedor(models.Model):  
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15) 
    correo = models.EmailField(max_length=50) 
class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
