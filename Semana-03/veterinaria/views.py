from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    EspecieForm,
    HistorialMedicoForm,
    InsumoForm,
    MascotaForm,
    ServicioForm,
)
from .models import Especie, HistorialMedico, Insumo, Mascota, Servicio

# ==========================================
# ESPECIES
# ==========================================
def lista_especies(request):
    especies = Especie.objects.all().order_by('nombre')
    return render(request, 'veterinaria/especie_list.html', {'especies': especies})


def crear_especie(request):
    form = EspecieForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La especie se creó correctamente.')
        return redirect('lista_especies')
    return render(request, 'veterinaria/especie_form.html', {'form': form})


def editar_especie(request, pk):
    especie = get_object_or_404(Especie, pk=pk)
    form = EspecieForm(request.POST or None, instance=especie)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La especie se actualizó correctamente.')
        return redirect('lista_especies')
    return render(request, 'veterinaria/especie_form.html', {'form': form, 'especie': especie})


def eliminar_especie(request, pk):
    if request.method == 'POST':
        especie = get_object_or_404(Especie, pk=pk)
        especie.delete()
        messages.success(request, 'La especie se eliminó correctamente.')
    return redirect('lista_especies')


# ==========================================
# INSUMOS
# ==========================================
def lista_insumos(request):
    insumos = Insumo.objects.all().order_by('nombre')
    return render(request, 'veterinaria/insumo_list.html', {'insumos': insumos})


def crear_insumo(request):
    form = InsumoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El insumo se creó correctamente.')
        return redirect('lista_insumos')
    return render(request, 'veterinaria/insumo_form.html', {'form': form})


def editar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    form = InsumoForm(request.POST or None, instance=insumo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El insumo se actualizó correctamente.')
        return redirect('lista_insumos')
    return render(request, 'veterinaria/insumo_form.html', {'form': form, 'insumo': insumo})


def eliminar_insumo(request, pk):
    if request.method == 'POST':
        insumo = get_object_or_404(Insumo, pk=pk)
        insumo.delete()
        messages.success(request, 'El insumo se eliminó correctamente.')
    return redirect('lista_insumos')


# ==========================================
# SERVICIOS
# ==========================================
def lista_servicios(request):
    servicios = Servicio.objects.all().order_by('nombre')
    return render(request, 'veterinaria/servicio_list.html', {'servicios': servicios})


def crear_servicio(request):
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El servicio se creó correctamente.')
        return redirect('lista_servicios')
    return render(request, 'veterinaria/servicio_form.html', {'form': form})


def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    form = ServicioForm(request.POST or None, instance=servicio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El servicio se actualizó correctamente.')
        return redirect('lista_servicios')
    return render(request, 'veterinaria/servicio_form.html', {'form': form, 'servicio': servicio})


def eliminar_servicio(request, pk):
    if request.method == 'POST':
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.delete()
        messages.success(request, 'El servicio se eliminó correctamente.')
    return redirect('lista_servicios')


# ==========================================
# MASCOTAS
# ==========================================
def lista_mascotas(request):
    
    buscar = request.GET.get('q')
    if buscar:
        mascotas = Mascota.objects.filter(nombre__icontains=buscar).order_by('nombre')
    else:
        mascotas = Mascota.objects.all().order_by('nombre')
        
    return render(request, 'veterinaria/mascota_list.html', {'mascotas': mascotas})


def crear_mascota(request):
    form = MascotaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota se creó correctamente.')
        return redirect('lista_mascotas')
    return render(request, 'veterinaria/mascota_form.html', {'form': form})


def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    form = MascotaForm(request.POST or None, instance=mascota)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'La mascota se actualizó correctamente.')
        return redirect('lista_mascotas')
    return render(request, 'veterinaria/mascota_form.html', {'form': form, 'mascota': mascota})


def eliminar_mascota(request, pk):
    if request.method == 'POST':
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        messages.success(request, 'La mascota se eliminó correctamente.')
    return redirect('lista_mascotas')


# ==========================================
# HISTORIALES MÉDICOS
# ==========================================
def lista_historiales(request):
    # Cumple Ejercicio 15: Orden descendente por fecha (-fecha)
    historiales = HistorialMedico.objects.all().order_by('-fecha')
    return render(request, 'veterinaria/historialmedico_list.html', {'historiales': historiales})


def crear_historial(request):
    form = HistorialMedicoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El historial médico se creó correctamente.')
        return redirect('lista_historiales')
    return render(request, 'veterinaria/historialmedico_form.html', {'form': form})


def editar_historial(request, pk):
    historial = get_object_or_404(HistorialMedico, pk=pk)
    form = HistorialMedicoForm(request.POST or None, instance=historial)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El historial médico se actualizó correctamente.')
        return redirect('lista_historiales')
    return render(request, 'veterinaria/historialmedico_form.html', {'form': form, 'historial': historial})


def eliminar_historial(request, pk):
    if request.method == 'POST':
        historial = get_object_or_404(HistorialMedico, pk=pk)
        historial.delete()
        messages.success(request, 'El historial médico se eliminó correctamente.')
    return redirect('lista_historiales')