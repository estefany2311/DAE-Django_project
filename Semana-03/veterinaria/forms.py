from django import forms

from .models import Especie, HistorialMedico, Insumo, Mascota, Servicio


class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        fields = '__all__'


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'


class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'
