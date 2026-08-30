from datetime import datetime

# Todas las fechas se almacenan como datetime naive (sin zona horaria),
# para que puedan compararse y ordenarse correctamente con sorted().
CITAS_DB = [
    {
        'id': 1,
        'paciente_nombre': 'Ana García',
        'paciente_telefono': '987654321',
        'fecha_hora': datetime(2026, 8, 29, 9, 0),
        'motivo_consulta': 'Ansiedad generalizada y manejo del estrés.',
        'estado': 'PENDIENTE',
    },
    {
        'id': 2,
        'paciente_nombre': 'Luis Pérez',
        'paciente_telefono': '912345678',
        'fecha_hora': datetime(2026, 8, 29, 10, 30),
        'motivo_consulta': 'Seguimiento terapéutico por depresión leve.',
        'estado': 'CONFIRMADA',
    },
    {
        'id': 3,
        'paciente_nombre': 'María López',
        'paciente_telefono': '998877665',
        'fecha_hora': datetime(2026, 8, 29, 12, 0),
        'motivo_consulta': 'Evaluación inicial para manejo emocional.',
        'estado': 'COMPLETADA',
    },
    {
        'id': 4,
        'paciente_nombre': 'Carlos Ruiz',
        'paciente_telefono': '923456789',
        'fecha_hora': datetime(2026, 8, 29, 15, 15),
        'motivo_consulta': 'Consulta por problemas de sueño.',
        'estado': 'CANCELADA',
    },
    {
        'id': 5,
        'paciente_nombre': 'Sofía Ramírez',
        'paciente_telefono': '934567890',
        'fecha_hora': datetime(2026, 8, 29, 17, 45),
        'motivo_consulta': 'Terapia de pareja y comunicación.',
        'estado': 'PENDIENTE',
    },
]
