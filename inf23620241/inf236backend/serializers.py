from rest_framework import serializers
from .models import Motor, Camion, AsignacionMotorCamion, Incident, Asign


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

    # Momentaneo para el hito 4, se sobreescribe el metodo save para guardar en la base de datos en JSON
    def save(self):
        import datetime
        for key, value in self.validated_data.items(): # Momentaneo formatamos las fechas a string para registrarlas en la (momentanea) base de datos en JSON
            if isinstance(value, datetime.date) :
                date = value.strftime("%Y-%m-%d")
                self.validated_data[key] = date
        
        import json
        with open('./inf236backend/tempDB/incidents.json') as incidentsDB:
            data = json.load(incidentsDB)
        data.append(self.validated_data)

        with open('./inf236backend/tempDB/incidents.json', 'w') as newIncidentsDB:
	        json.dump(data, newIncidentsDB)

class AsignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asign
        fields = '__all__'