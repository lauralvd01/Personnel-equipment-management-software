from django.db import models

# Create your models here.

# Model creation with its fields
# Add as many models/fields as necessary.
class Motor(models.Model):
    id_motor = models.AutoField(primary_key=True, default=0)
    n_serie = models.CharField(max_length=256, default="")
    operativo = models.BooleanField(default=True)
    tiempo_en_uso = models.IntegerField(null=True, blank=True)
    fecha_inicio = models.DateTimeField(default=None)
    durabilidad = models.IntegerField(null=True, blank=True)

class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True, default=0)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256, default="")
    n_serie = models.CharField(max_length=256, default="")

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True, default=0)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    n_serie = models.CharField(max_length=256, default="")
    fecha_inicio = models.DateTimeField(default=None)
    durabilidad = models.IntegerField(null=True, blank=True)

class Camion(models.Model):
    id_camion = models.AutoField(primary_key=True, default=0)
    n_serie = models.CharField(max_length=256, default="")
    placa = models.CharField(max_length=256, default="")
    estado = models.CharField(max_length=256, default="")
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    durabilidad = models.IntegerField(null=True, blank=True)

class AsignacionMotorCamion(models.Model):
    id_asignacion = models.AutoField(primary_key=True, default=0)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(default=None)
    fecha_desasignacion = models.DateTimeField(null=True, blank=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, default=0)
    rut = models.CharField(max_length=256, default="")
    contrasena = models.CharField(max_length=256, default="")
    nombre = models.CharField(max_length=256, default="")
    apellido = models.CharField(max_length=256, default="")
    fecha_registro = models.DateTimeField(default=None)
    rol = models.CharField(max_length=256, default="")
    turno = models.CharField(max_length=256, default="")


class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True, default=0)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    descripcion_problema = models.TextField()
    descripcion_trabajo_necesario = models.TextField()
    fecha_incidencia = models.DateTimeField(default=None)
    fecha_inicio_trabajo = models.DateTimeField(null=True, blank=True)
    fecha_fin_trabajo = models.DateTimeField(null=True, blank=True)
    solucionado = models.BooleanField(default=False)


# Modelo para Hito 4, en un futuro se eliminará y se trabajarán con los modelos vistos arriba

class Incident(models.Model):
    motor_id = models.CharField(max_length=100)
    mechanic_id = models.CharField(max_length=100)
    incident_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    solved = models.BooleanField()
    problem_description = models.TextField()
    work_to_do = models.TextField()

    def __str__(self):
        return self.motor_id