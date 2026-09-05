from django.contrib import admin

from .models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
	list_display = ('paciente_nombre', 'fecha_hora', 'estado')
	list_filter = ('estado', 'fecha_hora')
	search_fields = ('paciente_nombre', 'paciente_telefono')
