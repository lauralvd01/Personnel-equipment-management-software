from rest_framework import serializers
from .models import Motor, Camion, AsignacionMotorCamion, Incident


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


#Momentaneo solo para Hito 4
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'