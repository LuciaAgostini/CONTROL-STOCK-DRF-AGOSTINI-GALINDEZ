# Tercer Práctico DRF

**Ingeniería de Software – Facundo Lemo**

**Agostini – Galindez**

Proyecto de API de control de stock desarrollado con Django REST Framework.

## Cómo ejecutar el proyecto

**1. Instalar las dependencias**

```bash
uv sync
```

**2. Aplicar las migraciones**

```bash
uv run python src/manage.py migrate
```

**3. Crear un usuario**

```bash
uv run python src/manage.py createsuperuser
```

**4. Iniciar el servidor**

```bash
uv run python src/manage.py runserver
```

La API estará disponible en:

`http://127.0.0.1:8000/api/`