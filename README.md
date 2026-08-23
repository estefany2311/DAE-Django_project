# django_project

## Descripcion
Laboratorio Django 5 con una aplicacion `core` que muestra un listado de objetos `Item` y permite administrarlos desde Django Admin.

## Requisitos
- Python 3.13.14 (o Python 3.13 compatible)
- Windows PowerShell o CMD
- Django 5.2.17

## Estructura
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
        ├── migrations/
        └── templates/
            ├── base.html
            └── core/item_list.html
```

## Instalacion en Windows
Desde la carpeta `django_project`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En CMD, la activacion es:

```bat
venv\Scripts\activate.bat
```

## Migraciones y superusuario
Desde `django_project\src` y con `venv` activo:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

El comando de superusuario solicita los datos directamente; no se incluyen credenciales en este repositorio.

## Ejecutar el servidor

```powershell
python manage.py runserver
```

- Sitio: http://127.0.0.1:8000/
- Administrador: http://127.0.0.1:8000/admin/

## Modelo Item
`Item` contiene `name` (texto), `description` (texto opcional) y `created_at` (fecha y hora automatica de creacion). La vista `item_list` consulta todos los items y los envia a `core/item_list.html`, que hereda de `base.html`.
