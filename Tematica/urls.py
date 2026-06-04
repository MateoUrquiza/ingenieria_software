from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    home,
    hombre,
    productos,
    crear_producto,
    editar_producto,
    eliminar_producto
)

urlpatterns = [
    path("", home, name="home"),
    path("hombre/", hombre, name="hombre"),

    path("productos/", productos, name="productos"),
    path("productos/crear/", crear_producto, name="crear_producto"),
    path("productos/editar/<int:id>/", editar_producto, name="editar_producto"),
    path("productos/eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),

    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]