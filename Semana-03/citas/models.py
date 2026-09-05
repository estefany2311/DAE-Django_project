from django.db import models


class Cita(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        COMPLETADA = 'COMPLETADA', 'Completada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    paciente_nombre = models.CharField(max_length=100)
    paciente_telefono = models.CharField(max_length=9)
    fecha_hora = models.DateTimeField()
    motivo_consulta = models.TextField()
    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )

    class Meta:
        ordering = ['fecha_hora']

    def __str__(self):
        return f'{self.paciente_nombre} - {self.fecha_hora:%d/%m/%Y %H:%M}'
