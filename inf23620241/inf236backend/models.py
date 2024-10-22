from typing import Any
from django.db import models

# Create your models here.

# Model creation with its fields
# Add as many models/fields as necessary.
class Motor(models.Model):
    id_motor = models.AutoField(primary_key=True)
    n_serie = models.CharField(max_length=256, default="XXX")
    operativo = models.BooleanField(default=True)
    tiempo_en_uso = models.IntegerField(default=0)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    durabilidad = models.IntegerField(default=0) # Durabilidad en meses

class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256, default="Nombre")
    n_serie = models.CharField(max_length=256, default="XXX")

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256, default="Nombre")
    n_serie = models.CharField(max_length=256, default="XXX")
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    durabilidad = models.IntegerField(default=0)

class Camion(models.Model):
    id_camion = models.AutoField(primary_key=True)
    n_serie = models.CharField(max_length=256, default="XXX")
    placa = models.CharField(max_length=256, default="Placa")
    estado = models.CharField(max_length=256, default="Operativo")
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    durabilidad = models.IntegerField(default=0)

class AsignacionMotorCamion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_desasignacion = models.DateTimeField(null=True, blank=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=256, default="RUT")
    contrasena = models.CharField(max_length=256, default="Contrasena")
    nombre = models.CharField(max_length=256, default="Nombre")
    apellido = models.CharField(max_length=256, default="Apellido")
    fecha_registro = models.DateTimeField(auto_now_add=True, blank=True)
    rol = models.CharField(max_length=256, default="mecanico")
    turno = models.CharField(max_length=256, default="4x7")

class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    fecha_incidencia = models.DateTimeField(auto_now_add=True, blank=True)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, null=True)
    mecanicos_asociados = models.TextField(default="", null=True, blank=True)
    descripcion_problema = models.TextField(default="", null=True, blank=True)
    descripcion_trabajo_necesario = models.TextField(default="", null=True, blank=True)
    fecha_inicio_trabajo = models.DateTimeField(null=True, blank=True)
    descripcion_trabajo_hecho = models.TextField(default="", null=True, blank=True)
    fecha_fin_trabajo = models.DateTimeField(null=True, blank=True)
    solucionado = models.BooleanField(default=False)
    mecanico_asignado = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    # Caso de que la incidencia tenga varios mecanicos asociados --> Por hacer (necesita construir una tabla mas)

class Antecedente(models.Model):
    antecedente_id = models.AutoField(primary_key=True)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    problem_description = models.TextField(default="", null=True, blank=True)
    antecedente_date = models.DateTimeField(null=True, blank=True)






################################################################################

# Modelos para Hito 4, en un futuro se eliminarán y se trabajarán con los modelos vistos arriba

# class Asign(models.Model):
#     motor_id = models.CharField(default="", max_length=100)
#     camion_id = models.CharField(default="", max_length=100)
#     asign_date = models.CharField(default="", max_length=100)
#     unassign_date = models.CharField(default="", max_length=100)

# # Definiciones de funciones NO usadas
#     def filterByMotor(motor_id):
#         import json
#         with open('./inf236backend/tempDB/asign.json') as incidentsDB:
#             data = json.load(incidentsDB)
#         filtered_data = [asign for asign in data if f"{asign['motor_id']}" == motor_id]
#         return filtered_data
    
#     def filterByCamion(camion_id):
#         import json
#         with open('./inf236backend/tempDB/asign.json') as incidentsDB:
#             data = json.load(incidentsDB)
#         filtered_data = [asign for asign in data if f"{asign['camion_id']}" == camion_id]
#         return filtered_data
#Definiciones de funciones NO usadas

####################################################
#class Incident(models.Model):
#    motor_id = models.CharField(default="", blank=True, max_length=100)
#    incident_date = models.CharField(default="", blank=True, max_length=100)
#    problem_description = models.TextField(default="", blank=True)
#    mechanics_associated = models.TextField(default="", blank=True)
#    work_to_do = models.TextField(default="", blank=True)
#    mechanic_id = models.CharField(default="", blank=True, max_length=100)
#    start_date = models.CharField(default="", blank=True, max_length=100)
#    end_date = models.CharField(default="", blank=True, max_length=100)
#    solved = models.BooleanField(default=False)
#    id = models.IntegerField(primary_key=True)

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


######################################################
#    def all():
#        import json
#        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
#            data = json.load(incidentsDB)
#        return data
#    
#    def filterByMotor(motor_id):
#        import json
#        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
#            data = json.load(incidentsDB)
#        filtered_data = [incident for incident in data if f"{incident['motor_id']}" == motor_id]
#        return filtered_data
#    
#    def filterByMechanic(mechanic_id):
#        import json
#        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
#            data = json.load(incidentsDB)
#        print(data)
#        filtered_data = [incident for incident in data if 'mechanic_id' in incident.keys() and f"{incident['mechanic_id']}" == mechanic_id]
#        return filtered_data
#    
#    def getById(incident_id):
#        import json
#        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
#            data = json.load(incidentsDB)
#        for incident in data:
#            if incident['id'] == incident_id:
#                return incident
#        return None