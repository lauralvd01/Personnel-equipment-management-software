from rest_framework import serializers
from .models import Motor, Sistema, Componente, Camion, AsignacionMotorCamion, Usuario, Incidencia, Antecedente
from datetime import datetime


# Serializers are in charge to render arbitrary data types (json, URL encode forms, XML's) to python-like objects
class MotorSerializer(serializers.ModelSerializer):
    # This will tell which fields django will use while processing the view.
    class Meta:
        model = Motor
        fields = '__all__'

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'

class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'

class AsignacionMotorCamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionMotorCamion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = '__all__'

class AntecedenteSerializer(serializers.ModelSerializer):
    patente = serializers.CharField(write_only=True, required = True)
    fecha_registro = serializers.DateTimeField(required = True)
    usuario = serializers.ReadOnlyField(source='usuario.id_usuario')
    motor = serializers.SerializerMethodField()

    class Meta:
        model = Antecedente
        fields = '__all__'

    def getMotor(self, obj):
        try:
            asignacion = AsignacionMotorCamion.objects.filter(camion=obj.camion).latest('fecha_asignacion')
            return asignacion.motor.id_motor
        except AsignacionMotorCamion.DoesNotExist:
            raise serializers.ValidationError("No hay un motor asignado para este camión.")
        
    def validate_fecha_registro(self, value):
        if value > datetime.now():
            raise serializers.ValidationError("La fecha no puede ser en el futuro.")
        return value
    
    def create(self, validated_data):
        patente = validated_data.pop('patente')

        try:
            camion = Camion.objects.get(patente=patente)
        except Camion.DoesNotExist:
            raise serializers.ValidationError("No existe un camión con esa patente.")

        antecedente = Antecedente.objects.create(
            camion = camion,
            usuario = self.context['request'].user,
            **validated_data
        )
        return antecedente







# #Momentaneo solo para Hito 4

# class AsignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Asign
#         fields = '__all__'


# def readData(file):
#     import json
#     with open(file) as my_file:
#         data = json.load(my_file)
#     return data

# def saveData(file,data):
#     import json
#     with open(file, 'w') as new_file:
#         json.dump(data, new_file)

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