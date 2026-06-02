from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Proveedor(models.Model):  
    nombre = models.CharField(_("Nombre del Proveedor"), max_length=100)
    telefono = models.CharField(_("Teléfono"), max_length=15) 
    correo = models.EmailField(_("Correo Electrónico"), max_length=50) 
    
    usuario_responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name="proveedores_asignados",
        verbose_name=_("Empleado responsable")
    )

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre