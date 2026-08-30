# Instrucciones del laboratorio

## Objetivo
Construir y mantener un proyecto Django 5 llamado `django_project`, con una aplicacion `core` y un listado de objetos `Item`.

## Entorno y estructura
- Python utilizado: 3.13.14.
- Django utilizado: 5.2.17.
- El entorno virtual obligatorio es `venv/` en la raiz del proyecto.
- Hay que activar `venv` antes de instalar dependencias o ejecutar comandos Django.
- `manage.py` esta en `src/manage.py`.
- La configuracion esta en `src/config/settings.py`.
- Las URLs principales estan en `src/config/urls.py`.

La estructura esperada es:

```text
django_project/
├── CLAUDE.md
├── README.md
├── requirements.txt
├── .gitignore
├── venv/
└── src/
    ├── manage.py
    ├── config/
    └── core/
```

## Aplicacion y modelo
La aplicacion se llama `core` y esta registrada en `INSTALLED_APPS`.

El modelo `Item`, definido en `src/core/models.py`, tiene exactamente:
- `name`: `CharField`.
- `description`: `TextField` opcional.
- `created_at`: `DateTimeField` con `auto_now_add=True`.

Cualquier cambio al modelo requiere ejecutar `python manage.py makemigrations` y `python manage.py migrate` desde `src`.

## Vista, URLs y templates
La vista `item_list` obtiene todos los objetos `Item` y los envia con el contexto `items`.

- La URL `/` incluye las URLs de `core`.
- La plantilla base es `src/core/templates/base.html`.
- El listado es `src/core/templates/core/item_list.html`.
- El listado debe heredar mediante `{% extends "base.html" %}` y conservar los bloques `{% for %}` y `{% empty %}`.

## Administrador
`Item` debe permanecer registrado en `src/core/admin.py`. El superusuario se crea con `python manage.py createsuperuser`; nunca se deben inventar, guardar ni compartir credenciales.

## Comandos principales
Desde `django_project`:

```powershell
.\venv\Scripts\Activate.ps1
```

Desde `django_project\src`:

```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Reglas para modificar el proyecto
- Usar siempre el entorno virtual `venv`.
- Revisar archivos existentes antes de modificarlos.
- Mantener `manage.py` en `src/` y evitar una estructura `src/config/config/`.
- Ejecutar `python manage.py check` despues de cambios relevantes.
- No guardar contrasenas, claves ni archivos locales sensibles en Git.
- No subir cambios a GitHub sin autorizacion explicita.
