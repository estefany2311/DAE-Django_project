from django.contrib import admin
from .models import (
    Especie,
    Insumo,
    Servicio,
    Mascota,
    HistorialMedico,
    PerfilVeterinario,
    FichaMedica,
    CitaMedica,
    DetalleReceta,
    Factura,
)
# INLINES
#muestra datos relacionados 
class FichaMedicaInline(admin.StackedInline):
    model = FichaMedica
    can_delete = True
    verbose_name_plural = 'Ficha Médica Asociada (Relación 1:1)'
    extra = 1  # Muestra un formulario apilado para completar los datos

# muestra registros relacionados en forma de tabla
class DetalleRecetaInline(admin.TabularInline):
    model = DetalleReceta
    extra = 1  # Ofrece una fila vacía para agregar insumos recetados
    fields = ('insumo', 'cantidad', 'indicaciones_uso')
    
# MODELADMINS
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    # list_display muestra las columnsas que se dejaran ver 
    list_display = ('id', 'nombre', 'edad', 'dueno_nombre')
    # search_fields habilita el buscador por nombre de la mascota o dueño
    search_fields = ('nombre', 'dueno_nombre')
    
    #agregamos un filtro por edad para facilitar la búsqueda de mascotas según su edad
    list_filter = ('edad',)
    #Incorporamos el Inline 1:1 dentro de Mascota
    inlines = [FichaMedicaInline]


@admin.register(PerfilVeterinario)
class PerfilVeterinarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'colegiatura', 'especialidad', 'telefono')
    search_fields = ('colegiatura', 'especialidad')
    
    list_filter = ('especialidad',)
    


@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'veterinario', 'fecha_hora', 'estado', 'motivo')
    search_fields = ('motivo',)
    list_display_links=('id', 'mascota')
    list_filter = ('estado', 'fecha_hora')
    inlines = [DetalleRecetaInline]
    
    


# Registro simple de las demás entidades
admin.site.register(Especie)
admin.site.register(Insumo)
admin.site.register(Servicio)
admin.site.register(HistorialMedico)
admin.site.register(FichaMedica)
admin.site.register(DetalleReceta)
admin.site.register(Factura)