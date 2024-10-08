from rest_framework import serializers
from .models import Motor, Camion, AsignacionMotorCamion, Incident, Asign, Record, Records


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

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'  # Asegúrate de que incluye los campos que deseas

    def save(self):
        data = readData('./inf236backend/tempDB/records.json')
        if len(data) == 0:
            self.validated_data['id'] = 1
        else:
            self.validated_data['id'] = data[-1]['id'] + 1
        data.append(self.validated_data)
        saveData('./inf236backend/tempDB/records.json',data)


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

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
    
    def save(self):
        data = readData('./inf236backend/tempDB/incidents.json')
        if len(data) == 0:
            self.validated_data['id'] = 1
        else:
            self.validated_data['id'] = data[-1]['id'] + 1
        data.append(self.validated_data)
        saveData('./inf236backend/tempDB/incidents.json',data)
    
    @staticmethod
    def update_incident(new_data):
        data = readData('./inf236backend/tempDB/incidents.json')
        for index, incident in enumerate(data):

            if incident['id'] == new_data['id']:
                print("Found incident to update: ",data[index])
                data[index] = new_data
                print("Updated incident: ",data[index])
                break
        saveData('./inf236backend/tempDB/incidents.json',data)

    @staticmethod
    def merge(old, data):
        new_data = {}
        for key in data:
            if key in old :
                if data[key] is not None :
                    new_data[key] = data[key]
                else:
                    new_data[key] = old[key]
            else :
                new_data[key] = data[key]
        IncidentSerializer.update_incident(new_data)
        return new_data
    

