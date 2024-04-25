from django.db import models

# Create your models here.

# Model creation with its fields
# Add as many models/fields as necessary.
class Motor(models.Model):
    n_serie = models.CharField(max_length=256)
    operativo = models.BooleanField(default=True)
    tiempo_en_uso = models.IntegerField(null=True, blank=True)

class Camion(models.Model):
    estado = models.CharField(max_length=256)

class AsignacionMotorCamion(models.Model):
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_desasignacion = models.DateTimeField(null=True, blank=True)