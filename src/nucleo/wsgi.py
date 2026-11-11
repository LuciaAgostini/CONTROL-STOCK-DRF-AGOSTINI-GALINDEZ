"""
Configuración WSGI para el proyecto nucleo.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nucleo.settings")

application = get_wsgi_application()
