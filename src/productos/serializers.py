from rest_framework import serializers

from .models import Producto, Proveedor


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = [
            "id",
            "nombre",
            "telefono",
            "email",
            "direccion",
        ]
        read_only_fields = ["id"]


class ProductoSerializer(serializers.ModelSerializer):

    stock_bajo = serializers.ReadOnlyField()

    proveedor = ProveedorSerializer(read_only=True)

    proveedor_id = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all(),
        source="proveedor",
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "sku",
            "categoria",
            "precio",
            "cantidad_stock",
            "stock_minimo",
            "activo",
            "stock_bajo",
            "proveedor",
            "proveedor_id",
            "creado",
            "actualizado",
        ]

        read_only_fields = [
            "id",
            "creado",
            "actualizado",
        ]