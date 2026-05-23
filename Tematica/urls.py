from django.urls import path

from .views import home, ropa, productos, crear_producto, editar_producto, eliminar_producto

urlpatterns=[
    path('', home, name="home"),
    path('ropa/', ropa, name="ropa"),
    path("productos/", productos, name="productos"),
    path("productos/crear/", crear_producto, name="crear_producto"),
    path("productos/editar/<int:id>/", editar_producto, name="editar_producto"),
    path("productos/eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),
]