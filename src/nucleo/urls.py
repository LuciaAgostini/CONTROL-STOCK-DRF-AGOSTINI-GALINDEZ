from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def raiz(request):
    return redirect("producto-list")


urlpatterns = [
    path("", raiz, name="raiz"),
    path("admin/", admin.site.urls),
    path("api/", include("productos.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]