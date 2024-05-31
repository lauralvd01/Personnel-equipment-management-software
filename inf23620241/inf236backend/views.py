from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Motor, Camion, AsignacionMotorCamion
from .serializers import MotorSerializer, CamionSerializer, AsignacionMotorCamionSerializer

# Create your views here.
# Views are in charge of the business logic of the application
# Class ModelViewSet gives us many easy access to CRUD operations (Instead of creating it ourselves)

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer

class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class AsignacionMotorCamionViewSet(viewsets.ModelViewSet):
    queryset = AsignacionMotorCamion.objects.all()
    serializer_class = AsignacionMotorCamionSerializer
###################################### A partir de acá se hacen pruebas de conexión Controlador-Vista ####################################################################
# Nueva vista para manejar la solicitud POST del formulario de incidencias

@api_view(['POST'])

def login_view(request):
    role = request.data.get('role')
    password = request.data.get('password')
    
    if role == '123456789' and password == 'holamundo':
        return Response({'success': True}, status=status.HTTP_200_OK)
    else:
        return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


def handle_incident(request):
    data = request.data
    # Procesa los datos del formulario según tus necesidades
    # Por ejemplo, puedes guardar los datos en la base de datos o realizar otras operaciones

    # Aquí puedes realizar validaciones y otras lógicas de negocio
    
    motor_id = data.get('motorId')
    mechanic_id = data.get('mechanicId')
    incident_date = data.get('incidentDate')
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    solved = data.get('solved')
    problem_description = data.get('problemDescription')
    work_to_do = data.get('workToDo')

    # Ejemplo simple de validación y respuesta
    if not motor_id or not mechanic_id:
        return Response({'error': 'Faltan campos obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    # Aquí puedes crear una nueva instancia de un modelo, si es necesario
    # nuevo_incidente = Incidente.objects.create(
    response_data = {
        'motorId': motor_id,
        'mechanicId': mechanic_id,
        'incidentDate': incident_date,
        'startDate': start_date,
        'endDate': end_date,
        'solved': solved,
        'problemDescription': problem_description,
        'workToDo': work_to_do,
        'message': 'Formulario recibido correctamente'
    }

    # Responder con un mensaje de éxito
    return Response(response_data, status=status.HTTP_200_OK)
