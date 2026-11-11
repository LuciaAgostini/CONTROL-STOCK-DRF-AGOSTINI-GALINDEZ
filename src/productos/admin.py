from django.contrib import admin

from .models import Producto, Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "telefono",
        "email",
        "direccion",
    )

    search_fields = (
        "nombre",
        "telefono",
        "email",
    )


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "sku",
        "categoria",
        "precio",
        "cantidad_stock",
        "stock_minimo",
        "proveedor",
        "activo",
    )

    search_fields = (
        "nombre",
        "sku",
        "categoria",
    )

    list_filter = (
        "activo",
        "categoria",
        "proveedor",
    )