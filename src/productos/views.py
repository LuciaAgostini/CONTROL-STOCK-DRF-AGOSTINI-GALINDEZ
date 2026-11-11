from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Producto, Proveedor
from .serializers import ProductoSerializer, ProveedorSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]


class ProveedorConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related("proveedor").all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="ajustar-stock")
    def ajustar_stock(self, request, pk=None):
        cantidad = request.data.get("cantidad")

        if cantidad is None:
            return Response(
                {"detail": "Debés enviar el campo 'cantidad'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if isinstance(cantidad, bool):
            return Response(
                {"detail": "La cantidad debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cantidad_entera = int(cantidad)
        except (TypeError, ValueError):
            return Response(
                {"detail": "La cantidad debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if str(cantidad_entera) != str(cantidad):
            return Response(
                {"detail": "La cantidad debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():
            producto = get_object_or_404(
                self.get_queryset().select_for_update(),
                pk=pk
            )

            nuevo_stock = producto.cantidad_stock + cantidad_entera

            if nuevo_stock < 0:
                return Response(
                    {"detail": "No hay stock suficiente para esa salida."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            producto.cantidad_stock = nuevo_stock
            producto.save(update_fields=["cantidad_stock"])

        serializer = self.get_serializer(producto)

        return Response(serializer.data, status=status.HTTP_200_OK)