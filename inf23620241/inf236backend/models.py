from typing import Any
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

class Record(models.Model):
    record_id = models.AutoField(primary_key=True, default= 0)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    problem_description = models.TextField()
    record_date = models.DateTimeField(default=None)











# Modelos para Hito 4, en un futuro se eliminarán y se trabajarán con los modelos vistos arriba

class Asign(models.Model):
    motor_id = models.CharField(default="", max_length=100)
    camion_id = models.CharField(default="", max_length=100)
    asign_date = models.CharField(default="", max_length=100)
    unassign_date = models.CharField(default="", max_length=100)
    
    def __str__(self):
        return f"Motor {self.motor_id} - Camión {self.camion_id} ({self.asign_date} a {self.unassign_date})"

    def filterByMotor(motor_id):
        import json
        with open('./inf236backend/tempDB/asign.json') as incidentsDB:
            data = json.load(incidentsDB)
        filtered_data = [asign for asign in data if f"{asign['motor_id']}" == motor_id]
        return filtered_data
    
    def filterByCamion(camion_id):
        import json
        with open('./inf236backend/tempDB/asign.json') as incidentsDB:
            data = json.load(incidentsDB)
        filtered_data = [asign for asign in data if f"{asign['camion_id']}" == camion_id]
        return filtered_data


class Incident(models.Model):
    motor_id = models.CharField(default="", blank=True, max_length=100)
    incident_date = models.CharField(default="", blank=True, max_length=100)
    problem_description = models.TextField(default="", blank=True)
    mechanics_associated = models.TextField(default="", blank=True)
    work_to_do = models.TextField(default="", blank=True)
    mechanic_id = models.CharField(default="", blank=True, max_length=100)
    start_date = models.CharField(default="", blank=True, max_length=100)
    end_date = models.CharField(default="", blank=True, max_length=100)
    solved = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True, default=0)

    # def __init__(self, report) :
    #     print("Creating incident with data: ", report)
    #     import datetime
    #     self.motor_id = report['motor_id']
    #     if isinstance(report['incident_date'], datetime.date) :
    #             date = report['incident_date'].strftime("%Y-%m-%d")
    #             self.incident_date = date
    #     else:
    #         self.incident_date = report['incident_date']
    #     self.problem_description = report['problem_description']
    #     self.mechanics_associated = report['mechanics_associated']
    #     self.work_to_do = report['work_to_do']
    #     self.mechanic_id = ""
    #     self.start_date = ""
    #     self.end_date = ""
    #     self.solved = False

    def all():
        import json
        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
            data = json.load(incidentsDB)
        return data
    
    def filterByMotor(motor_id):
        import json
        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
            data = json.load(incidentsDB)
        filtered_data = [incident for incident in data if f"{incident['motor_id']}" == motor_id]
        return filtered_data
    
    def filterByMechanic(mechanic_id):
        import json
        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
            data = json.load(incidentsDB)
        print(data)
        filtered_data = [incident for incident in data if 'mechanic_id' in incident.keys() and f"{incident['mechanic_id']}" == mechanic_id]
        return filtered_data
    
    def getById(incident_id):
        import json
        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
            data = json.load(incidentsDB)
        for incident in data:
            if incident['id'] == incident_id:
                return incident
        return None