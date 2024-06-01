from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Motor, Camion, AsignacionMotorCamion, Incident
from .serializers import MotorSerializer, CamionSerializer, AsignacionMotorCamionSerializer, IncidentSerializer



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

# Modificación momentánea para hito 4
@api_view(['POST'])
def handle_incident(request):
    if request.method == 'POST':
        print(f"Request data: {request.data}")
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_incidents(request):
    motor_id = request.query_params.get('motor_id', None)
    if motor_id is not None:
        incidents = Incident.objects.filter(motor_id=motor_id)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Motor ID no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
