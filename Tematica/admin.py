from django.contrib import admin

# Register your models here.

from .models import Producto,Proveedor

admin.site.register(Producto)

@admin.register(Proveedor)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se verán en el listado
    list_display = ('nombre', 'telefono', 'correo')
    # Filtros laterales (ideal para campos con opciones o fechas)
    list_filter = ('nombre',)
    
    # Barra de búsqueda (busca en los campos indicados)
    search_fields = ('correo',)


