from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import CitaForm
from .models import CITAS_DB


def normalizar_fecha(fecha):
    """Convierte fechas timezone-aware a naive para poder compararlas."""
    if hasattr(fecha, 'tzinfo') and fecha.tzinfo is not None:
        return fecha.replace(tzinfo=None)
    return fecha


def inicio(request):
    """Página de inicio con resumen de atención del centro psicológico."""
    total_citas = len(CITAS_DB)
    pendientes = sum(1 for cita in CITAS_DB if cita['estado'] == 'PENDIENTE')
    confirmadas = sum(1 for cita in CITAS_DB if cita['estado'] == 'CONFIRMADA')
    completadas = sum(1 for cita in CITAS_DB if cita['estado'] == 'COMPLETADA')
    canceladas = sum(1 for cita in CITAS_DB if cita['estado'] == 'CANCELADA')

    proximas_citas = sorted(
        CITAS_DB,
        key=lambda cita: normalizar_fecha(cita['fecha_hora'])
    )[:3]

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
    """Muestra la lista completa de citas en memoria."""
    q = request.GET.get('q', '').strip().lower()
    fecha = request.GET.get('fecha', '').strip()

    citas = CITAS_DB

    if q:
        citas = [
            cita for cita in citas
            if q in cita['paciente_nombre'].lower()
        ]

    if fecha:
        citas = [
            cita for cita in citas
            if cita['fecha_hora'].date().isoformat() == fecha
        ]

    total_citas = len(citas)
    pendientes = sum(1 for cita in citas if cita['estado'] == 'PENDIENTE')
    confirmadas = sum(1 for cita in citas if cita['estado'] == 'CONFIRMADA')
    completadas = sum(1 for cita in citas if cita['estado'] == 'COMPLETADA')
    canceladas = sum(1 for cita in citas if cita['estado'] == 'CANCELADA')

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
    """Actualiza el estado de una cita en memoria."""
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado', '').strip()
        for cita in CITAS_DB:
            if cita['id'] == cita_id:
                cita['estado'] = nuevo_estado
                messages.success(request, 'El estado de la cita fue actualizado.')
                break
    return redirect('lista_citas')


def eliminar_cita(request, cita_id):
    """Elimina una cita de la lista en memoria."""
    if request.method == 'POST':
        CITAS_DB[:] = [cita for cita in CITAS_DB if cita['id'] != cita_id]
        messages.success(request, 'La cita fue eliminada correctamente.')
    return redirect('lista_citas')


def crear_cita(request):
    """Registra una nueva cita en la base de datos en memoria."""
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            ultimo_id = max((cita['id'] for cita in CITAS_DB), default=0)
            fecha_hora = normalizar_fecha(form.cleaned_data['fecha_hora'])
            nueva_cita = {
                'id': ultimo_id + 1,
                'paciente_nombre': form.cleaned_data['paciente_nombre'],
                'paciente_telefono': form.cleaned_data['paciente_telefono'],
                'fecha_hora': fecha_hora,
                'motivo_consulta': form.cleaned_data['motivo_consulta'],
                'estado': form.cleaned_data['estado'],
            }
            CITAS_DB.append(nueva_cita)
            messages.success(request, 'La cita se registró correctamente.')
            return redirect('lista_citas')
    else:
        form = CitaForm()

    return render(request, 'citas/crear.html', {'form': form})


def detalle_cita(request, cita_id):
    """Permite ver el detalle específico del motivo de consulta de un paciente."""
    cita_encontrada = None
    for cita in CITAS_DB:
        if cita['id'] == cita_id:
            cita_encontrada = cita
            break

    if not cita_encontrada:
        raise Http404("La cita solicitada no existe.")

    return render(request, 'citas/detalle.html', {'cita': cita_encontrada})