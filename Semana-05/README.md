# 🐾 Sistema de Gestión Veterinaria - Django Admin Laboratorio 05

Proyecto desarrollado en Django para la gestión operativa y clínica de una veterinaria. En esta entrega se implementó la configuración avanzada del panel de administración nativo (**Django Admin**) para la gestión de entidades relacionales sin la necesidad de vistas front-end adicionales.

---

## Estructura del Dominio 

El modelo de datos está conformado por las siguientesentidades y sus respectivas relaciones relacionales:

1. **`Especie`**: Clasificación de animales (Canino, Felino, etc.).
2. **`Insumo`**: Productos de la farmacia veterinaria y medicamentos.
3. **`Servicio`**: Servicios médicos ofrecidos por la clínica.
4. **`Mascota`**: Datos principales de los pacientes (nombre, edad y dueño).
5. **`HistorialMedico`**: Registro clínico e historial de intervenciones.
6. **`PerfilVeterinario`**: Información del personal veterinario y colegiatura.
7. **`FichaMedica`**: Ficha técnica con chip, alergias y grupo sanguíneo.
8. **`CitaMedica`**: Registro de consultas, fechas y estados del turno.
9. **`DetalleReceta`**: Modelo intermedio (**Relación N:M entre `CitaMedica` e `Insumo`**) con atributos de cantidad e indicaciones.
10. **`Factura`**: Comprobantes de pago por atención o servicios.
---

## Configuración del Panel de Administración (`admin.py`)

La gestión administrativa fue personalizada utilizando herramientas avanzadas de `django.contrib.admin`:

### 1. Personalización de Vistas con `ModelAdmin`
* **`list_display`**: Configurado en `Mascota`, `CitaMedica`, `PerfilVeterinario`, `Insumo` y `Factura` para mostrar información estructurada en columnas.
* **`search_fields`**: Búsqueda dinámica en tiempo real por nombre de mascota, dueño, colegiatura, especialidad o motivo de consulta.
* **`list_filter`**: Filtros laterales para clasificar citas por `estado` o `fecha_hora`, y profesionales por `especialidad`.

### 2. Formulario Integrado con Inlines
* **`StackedInline` (Relación 1:1)**: Se implementó `FichaMedicaInline` dentro de `MascotaAdmin` para visualizar y editar el expediente clínico directamente en el formulario de la mascota.
* **`TabularInline` (Relación N:M)**: Se implementó `DetalleRecetaInline` dentro de `CitaMedicaAdmin` para prescribir insumos en formato de tabla dentro de la misma vista de la cita.

---
