from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    sku = models.CharField("Código SKU", max_length=30, unique=True)
    categoria = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5)
    activo = models.BooleanField(default=True)
    actualizado = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="productos"
    )

    class Meta:
        ordering = ["nombre"]

    @property
    def stock_bajo(self):
        return self.cantidad_stock <= self.stock_minimo

    def __str__(self):
        return f"{self.nombre} ({self.sku}) - stock: {self.cantidad_stock}"