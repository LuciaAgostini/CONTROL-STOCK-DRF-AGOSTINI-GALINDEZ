from rest_framework.routers import DefaultRouter

from .views import (
    ProductoViewSet,
    ProveedorViewSet,
    ProveedorConsultaViewSet,
)

router = DefaultRouter()

router.register(
    r"productos",
    ProductoViewSet,
    basename="producto"
)

router.register(
    r"proveedores",
    ProveedorViewSet,
    basename="proveedor"
)

router.register(
    r"proveedores-consulta",
    ProveedorConsultaViewSet,
    basename="proveedor-consulta"
)