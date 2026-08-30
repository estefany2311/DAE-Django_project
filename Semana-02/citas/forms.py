from django import forms
from django.utils import timezone


class CitaForm(forms.Form):
    paciente_nombre = forms.CharField(
        label='Paciente',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
    )
    paciente_telefono = forms.CharField(
        label='Teléfono',
        max_length=9,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 987654321'}),
    )
    fecha_hora = forms.DateTimeField(
        label='Fecha y hora',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
    )
    motivo_consulta = forms.CharField(
        label='Motivo de consulta',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describa el motivo de la consulta'}),
    )
    estado = forms.ChoiceField(
        label='Estado',
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('CONFIRMADA', 'Confirmada'),
            ('COMPLETADA', 'Completada'),
            ('CANCELADA', 'Cancelada'),
        ],
        initial='PENDIENTE',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

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