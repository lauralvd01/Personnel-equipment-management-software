from rest_framework import serializers
from .models import Motor, Camion, AsignacionMotorCamion, Incidencia, Asign, Usuario


# Serializers are in charge to render arbitrary data types (json, URL encode forms, XML's) to python-like objects
class MotorSerializer(serializers.ModelSerializer):
    # This will tell which fields django will use while processing the view.
    class Meta:
        model = Motor
        fields = '__all__'

class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'

class AsignacionMotorCamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionMotorCamion
        fields = '__all__'


class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = '__all__'
        read_only_fields = ('id_incidencia',)




#Momentaneo solo para Hito 4

class AsignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asign
        fields = '__all__'


def readData(file):
    import json
    with open(file) as my_file:
        data = json.load(my_file)
    return data

def saveData(file,data):
    import json
    with open(file, 'w') as new_file:
        json.dump(data, new_file)

#class IncidentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Incident
#        fields = '__all__'
#   
#
#    @staticmethod
#    def merge(old, data):
#        new_data = {}
#        for key in data:
#            if key in old :
#                if data[key] is not None :
#                    new_data[key] = data[key]
#                else:
#                    new_data[key] = old[key]
#            else :
#                new_data[key] = data[key]
#        IncidentSerializer.update_incident(new_data)
#        return new_data

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'rut', 'contrasena', 'nombre', 'apellido', 'fecha_registro', 'rol', 'turno']