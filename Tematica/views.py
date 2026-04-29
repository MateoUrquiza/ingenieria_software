
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    productos_destacados = [
        {
            "nombre": "Buzo negro cross",
            "precio": "$35.000",
            "imagen": "https://crossclothing.com.ar/wp-content/uploads/2023/07/riri-front-black-ok.jpg"
        },
        {
            "nombre": "Remera seleccion",
            "precio": "$24.500",
            "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeI8TkWPTrvB7yi-5CKPGORPClnaBWQoef8g&s"
        },
        {
            "nombre": "Pantalón Urbano",
            "precio": "$29.900",
            "imagen": "https://crossclothing.com.ar/wp-content/uploads/2025/12/CROSS-29889-1-1500x1875.jpg"
        },
    ]

    return render(request, "Tematica/index.html", {
        "productos": productos_destacados
    })

def ropa(request):
    productos_hombre = [
        {
            "nombre": "Campera Negra",
            "precio": "$42.000",
            "imagen": "https://http2.mlstatic.com/D_738221-MLA109683468575_032026-O.jpg"
        },
        {
            "nombre": "Remera Básica",
            "precio": "$14.900",
            "imagen": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=80"
        },
        {
            "nombre": "Jean Slim Fit",
            "precio": "$31.500",
            "imagen": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=900&q=80"
        },
        {
            "nombre": "Buzo Oversize",
            "precio": "$27.800",
            "imagen": "https://crossclothing.com.ar/wp-content/uploads/2025/04/HOODIE-CHROME-1.jpg"
        },
    ]

    return render(request, "Tematica/ropa.html", {
        "productos": productos_hombre
    })