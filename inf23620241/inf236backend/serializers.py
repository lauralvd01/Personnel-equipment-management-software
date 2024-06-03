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
    def merge(self, old, data):
        new_data = old
        for key in data:
            if key in data.keys() and data[key] is not None:
                new_data[key] = data[key]
        print("Merged data: of ",old," and ",data," = ",new_data)
        return IncidentSerializer(data=new_data)

    def update(self):
        data = readData('./inf236backend/tempDB/incidents.json')
        for index, incident in enumerate(data):
            if incident['id'] == self.validated_data['id']:
                print("Found incident to update: ",data[index])
                data[index] = self.validated_data
                print("Updated incident: ",data[index])
                break
        saveData('./inf236backend/tempDB/incidents.json',data)