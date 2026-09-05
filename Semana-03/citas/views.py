from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CitaForm
from .models import Cita


def inicio(request):
    """Página de inicio con resumen de atención del centro psicológico."""
    total_citas = Cita.objects.count()
    pendientes = Cita.objects.filter(estado=Cita.Estado.PENDIENTE).count()
    confirmadas = Cita.objects.filter(estado=Cita.Estado.CONFIRMADA).count()
    completadas = Cita.objects.filter(estado=Cita.Estado.COMPLETADA).count()
    canceladas = Cita.objects.filter(estado=Cita.Estado.CANCELADA).count()
    proximas_citas = Cita.objects.all()[:3]

    context = {
        'total_citas': total_citas,
        'pendientes': pendientes,
        'confirmadas': confirmadas,
        'completadas': completadas,
        'canceladas': canceladas,
        'proximas_citas': proximas_citas,
    }
    return render(request, 'citas/inicio.html', context)


def lista_citas(request):
    """Muestra la lista completa de citas."""
    q = request.GET.get('q', '').strip()
    fecha = request.GET.get('fecha', '').strip()

    citas = Cita.objects.all()

    if q:
        citas = citas.filter(paciente_nombre__icontains=q)

    if fecha:
        citas = citas.filter(fecha_hora__date=fecha)

    total_citas = citas.count()
    pendientes = citas.filter(estado=Cita.Estado.PENDIENTE).count()
    confirmadas = citas.filter(estado=Cita.Estado.CONFIRMADA).count()
    completadas = citas.filter(estado=Cita.Estado.COMPLETADA).count()
    canceladas = citas.filter(estado=Cita.Estado.CANCELADA).count()

    context = {
        'citas': citas,
        'total_citas': total_citas,
        'pendientes': pendientes,
        'confirmadas': confirmadas,
        'completadas': completadas,
        'canceladas': canceladas,
        'q': q,
        'fecha': fecha,
    }
    return render(request, 'citas/lista.html', context)


def actualizar_estado(request, cita_id):
    """Actualiza el estado de una cita."""
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado', '').strip()
        cita = get_object_or_404(Cita, pk=cita_id)
        if nuevo_estado in Cita.Estado.values:
            cita.estado = nuevo_estado
            cita.save(update_fields=['estado'])
            messages.success(request, 'El estado de la cita fue actualizado.')
    return redirect('lista_citas')


def eliminar_cita(request, cita_id):
    """Elimina una cita."""
    if request.method == 'POST':
        cita = get_object_or_404(Cita, pk=cita_id)
        cita.delete()
        messages.success(request, 'La cita fue eliminada correctamente.')
    return redirect('lista_citas')


def crear_cita(request):
    """Registra una nueva cita en la base de datos."""
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita se registró correctamente.')
            return redirect('lista_citas')
    else:
        form = CitaForm()

    return render(request, 'citas/crear.html', {'form': form})


def detalle_cita(request, cita_id):
    """Permite ver el detalle específico del motivo de consulta de un paciente."""
    cita = get_object_or_404(Cita, pk=cita_id)
    return render(request, 'citas/detalle.html', {'cita': cita})
