from django.db import models


class Especie(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Insumo(models.Model):
	nombre = models.CharField(max_length=100)
	stock = models.IntegerField(default=0)
	precio = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.nombre


class Servicio(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.nombre


class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	edad = models.IntegerField()
	dueno_nombre = models.CharField(max_length=100, verbose_name="Dueño")

	def __str__(self):
		return self.nombre


class HistorialMedico(models.Model):
	mascota = models.ForeignKey(
		Mascota,
		on_delete=models.CASCADE,
		related_name='historiales',
	)
	fecha = models.DateField()
	diagnostico = models.TextField()
	tratamiento = models.TextField()

	def __str__(self):
		return f'{self.mascota} - {self.fecha}'
