from django.db import models

# Create your models here.

# Model creation with its fields
# Add as many models/fields as necessary.
class Motor(models.Model):
    id_motor = models.AutoField(primary_key=True)
    n_serie = models.CharField(max_length=256)
    operativo = models.BooleanField(default=True)
    tiempo_en_uso = models.IntegerField(null=True, blank=True)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    durabilidad = models.IntegerField(null=True, blank=True)

class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256)
    n_serie = models.CharField(max_length=256)

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    n_serie = models.CharField(max_length=256)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    durabilidad = models.IntegerField(null=True, blank=True)

class Camion(models.Model):
    id_camion = models.AutoField(primary_key=True)
    n_serie = models.CharField(max_length=256)
    placa = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    durabilidad = models.IntegerField(null=True, blank=True)

class AsignacionMotorCamion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_desasignacion = models.DateTimeField(null=True, blank=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut = models.EmailField()
    contrasena = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=256)
    turno = models.CharField(max_length=256)


class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    descripcion_problema = models.TextField()
    descripcion_trabajo_necesario = models.TextField()
    fecha_incidencia = models.DateTimeField(auto_now_add=True)
    fecha_inicio_trabajo = models.DateTimeField(null=True, blank=True)
    fecha_fin_trabajo = models.DateTimeField(null=True, blank=True)
    solucionado = models.BooleanField(default=False)
