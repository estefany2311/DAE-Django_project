from django import forms
from django.utils import timezone

from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'paciente_nombre',
            'paciente_telefono',
            'fecha_hora',
            'motivo_consulta',
            'estado',
        ]
        labels = {
            'paciente_nombre': 'Paciente',
            'paciente_telefono': 'Teléfono',
            'fecha_hora': 'Fecha y hora',
            'motivo_consulta': 'Motivo de consulta',
            'estado': 'Estado',
        }
        widgets = {
            'paciente_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo',
            }),
            'paciente_telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 987654321',
            }),
            'fecha_hora': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'motivo_consulta': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describa el motivo de la consulta',
            }),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_paciente_telefono(self):
        telefono = self.cleaned_data['paciente_telefono'].strip()

        if not telefono.isdigit() or len(telefono) < 9:
            raise forms.ValidationError('El teléfono debe contener solo números y mínimo 9 dígitos.')

        return telefono

    def clean_fecha_hora(self):
        fecha_ingresada = self.cleaned_data.get('fecha_hora')

        if fecha_ingresada:
            ahora = timezone.now()

            # Ajuste de zona horaria para evitar errores al comparar
            if timezone.is_naive(fecha_ingresada):
                ahora = timezone.make_naive(ahora)

            if fecha_ingresada < ahora:
                raise forms.ValidationError('No se pueden agendar citas en fechas o horas pasadas.')

        return fecha_ingresada