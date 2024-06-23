from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Motor, Camion, AsignacionMotorCamion,  Asign, Usuario, Incidencia
from .serializers import MotorSerializer, CamionSerializer, AsignacionMotorCamionSerializer,  AsignSerializer, UsuarioSerializer, IncidenciaSerializer



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

# Modificación momentánea para hito 4
@api_view(['POST'])
def handle_incident(request):
    if request.method == 'POST':
        print(f"Request data: {request.data}")
        serializer = IncidenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def search_incidents(request):
#     motor_id = request.query_params.get('motor_id', None)
#     if motor_id is not None:
#         incidents = Incident.objects.filter(motor_id=motor_id)
#         serializer = IncidentSerializer(incidents, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response({'error': 'Motor ID no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
def search_asign(request):
    motor_id = request.query_params.get('motor_id', None)
    camion_id = request.query_params.get('camion_id', None)
    try:
        if motor_id is not None:
            asignaciones = AsignacionMotorCamion.objects.filter(motor_id=motor_id)
            serializer = AsignacionMotorCamionSerializer(asignaciones, many=True)
            print(asignaciones)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if camion_id is not None:
            asignaciones = AsignacionMotorCamion.objects.filter(camion_id=camion_id)
            serializer = AsignacionMotorCamionSerializer(asignaciones, many=True)
            print(asignaciones)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    except AsignacionMotorCamion.DoesNotExist:
        return Response({'error': 'No se encontraron asignaciones para el ID proporcionado'}, status=status.HTTP_404_NOT_FOUND)

#@api_view(['POST'])
#def login_bdd(request):
#    rut = request.data.get('rut')
#    contrasena = request.data.get('contrasena')
#    #print(f"Datos recibidos: rut={rut}, contrasena={contrasena}")
#    try:
#        usuario = Usuario.objects.get(rut=rut)
#        print(f"Usuario encontrado: rut={usuario.rut}, contrasena={usuario.contrasena}")
#        if usuario.contrasena == contrasena:  # Si la contraseña está hasheada, usar check_password
#            serializer = UsuarioSerializer(usuario)
#            return Response({'success': True, 'id': usuario.id_usuario}, status=status.HTTP_200_OK)
#        else:
#            return Response({'success': False, 'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
#    except Usuario.DoesNotExist:
#        return Response({'success': False, 'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)





@api_view(['POST'])
def submit_incident(request):
    serializer = IncidenciaSerializer(data=request.data)
    if serializer.is_valid():
        print(f"Serializer data: {serializer.validated_data}")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(f"Serializer errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllIncidents(request):
    incidents = Incidencia.all()
    if incidents is not None:
        serializer = IncidenciaSerializer(incidents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No incidencias encontradas'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_incidents(request):
    motor_id = request.query_params.get('motor_id', None)
    if motor_id is not None:
        incidents = Incidencia.filterByMotor(motor_id=motor_id)
        serializer = IncidenciaSerializer(incidents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    mechanic_id = request.query_params.get('mechanic_id', None)
    if mechanic_id is not None:
        incidents = Incidencia.filterByMechanic(mechanic_id=mechanic_id)
        serializer = IncidenciaSerializer(incidents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Motor ID no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def edit_incident(request):
    print(request.data)
    incident_id = request.data["id"]
    if incident_id is not None:
        incident = Incidencia.getById(incident_id)
        if incident is None:
            return Response({'error': 'Incidencia con este ID no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            new_incident = IncidenciaSerializer.merge(old=incident, data=request.data)
            return Response(new_incident, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error: Incidencia con este ID no encontrada'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_password(request):
    user_id = request.data["mechanic_id"]
    old_password = request.data["oldPassword"]
    new_password = request.data["newPassword"]
    valid_new_password = request.data["validNewPassword"]
    
    import json
    with open('inf236backend/tempDB/users.json') as my_file:
        data = json.load(my_file)
    
    for user in data:
        if f"{user['id_usuario']}" == user_id :
            if user['contrasena'] == old_password and new_password == valid_new_password:
                user['contrasena'] = new_password
                with open('inf236backend/tempDB/users.json', 'w') as my_file:
                    json.dump(data, my_file)
                return Response({'success': True}, status=status.HTTP_200_OK)
            else :
                return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def creacion_usuario(request):
    print(request.data)
    serializer = IncidenciaSerializer(data=request.data)
    if serializer.is_valid():
        print(f"Serializer data: {serializer.validated_data}")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(f"Serializer errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login_bdd(request):
    rut = request.data.get('rut')
    contrasena = request.data.get('contrasena')
    #print(f"Datos recibidos: rut={rut}, contrasena={contrasena}")
    try:
        usuario = Usuario.objects.get(rut=rut)
        print(f"Usuario encontrado: rut={usuario.rut}, contrasena={usuario.contrasena}")
        if usuario.contrasena == contrasena:  # Si la contraseña está hasheada, usar check_password
            serializer = UsuarioSerializer(usuario)
            return Response({'success': True, 'id': usuario.id_usuario}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
    except Usuario.DoesNotExist:
        return Response({'success': False, 'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)