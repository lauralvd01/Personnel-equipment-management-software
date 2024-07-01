from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Motor, Sistema, Componente, Camion, AsignacionMotorCamion, Usuario, Incidencia
from .serializers import MotorSerializer, SistemaSerializer, ComponenteSerializer, CamionSerializer, AsignacionMotorCamionSerializer, UsuarioSerializer,  IncidenciaSerializer



# Create your views here.
# Views are in charge of the business logic of the application
# Class ModelViewSet gives us many easy access to CRUD operations (Instead of creating it ourselves)

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer

class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class AsignacionMotorCamionViewSet(viewsets.ModelViewSet):
    queryset = AsignacionMotorCamion.objects.all()
    serializer_class = AsignacionMotorCamionSerializer

    def create(self, request, *args, **kwargs):
        serializer = AsignacionMotorCamionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Actualizar estado del camión
            camion_id = serializer.data['camion']
            camion = Camion.objects.get(id_camion=camion_id)
            camion.estado = 'Funcionando'
            if camion.fecha_inicio is None:
                print("Fecha de inicio asignada")
                camion.fecha_inicio = serializer.data['fecha_asignacion']
            camion.save()

            # Actualizar estado del motor
            motor_id = serializer.data['motor']
            motor = Motor.objects.get(id_motor=motor_id)
            if motor.fecha_inicio is None:
                motor.fecha_inicio = serializer.data['fecha_asignacion']
            motor.save()

            # Actualizar estado de los componentes de los sistemas del motor
            sistemas = Sistema.objects.filter(motor=motor_id)
            for sistema in sistemas:
                componentes = Componente.objects.filter(sistema=sistema.id_sistema)
                for componente in componentes:
                    if componente.fecha_inicio is None:
                        componente.fecha_inicio = serializer.data['fecha_asignacion']
                        componente.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer

    def create(self, request, *args, **kwargs):
        serializer = IncidenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Actualizar estado del camión
            camion_id = serializer.data['camion']
            camion = Camion.objects.get(id_camion=camion_id)
            camion.estado = 'En reparación'
            camion.save()

            # Actualizar estado del motor asociado al camión
            asignacion = AsignacionMotorCamion.objects.filter(camion=camion_id).first()
            motor_id = asignacion.motor.id_motor
            motor = Motor.objects.get(id_motor=motor_id)
            motor.operativo = False
            motor.save()

            # Actualizar incidencia con el motor
            incidencia = Incidencia.objects.get(id_incidencia=serializer.data['id_incidencia'])
            incidencia.motor = motor
            incidencia.save()

            new_serializer = IncidenciaSerializer(incidencia)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###################################### LOGIN ######################################################
@api_view(['POST'])
def login(request):
    rut = request.data.get('rut')
    contrasena = request.data.get('contrasena')
    try:
        usuario = Usuario.objects.get(rut=rut)
        if usuario.contrasena == contrasena:
            return Response({'success': True, 'id': usuario.id_usuario, 'rol': usuario.rol}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
    except Usuario.DoesNotExist:
        return Response({'success': False, 'message': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)


###################################### FILTRAR INCIDENCIAS ########################################
@api_view(['GET'])
def filtrar_incidencias(request):
    print(request.query_params)

    ######################################################### Get tareas pendientes
    mecanico_id = request.query_params.get('mecanico_asignado', None)
    solucionado = request.query_params.get('solucionado', None)
    if (mecanico_id is not None) and (solucionado is not None):
        incidencias = Incidencia.objects.filter(mecanico_asignado=mecanico_id, solucionado=solucionado)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    ######################################################### Filtro por camion, motor y fecha
    camion_id = request.query_params.get('camion', None)
    motor_id = request.query_params.get('motor', None)
    fecha = request.query_params.get('fecha', None)
    if (camion_id is not None) and (motor_id is not None) and (fecha is not None):
        incidencias = Incidencia.objects.filter(camion=camion_id, motor=motor_id, fecha_incidencia__date=fecha)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if (camion_id is not None) and (motor_id is not None):
        incidencias = Incidencia.objects.filter(camion=camion_id, motor=motor_id)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if (camion_id is not None) and (fecha is not None):
        incidencias = Incidencia.objects.filter(camion=camion_id, fecha_incidencia__date=fecha)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if (motor_id is not None) and (fecha is not None):
        incidencias = Incidencia.objects.filter(motor=motor_id, fecha_incidencia__date=fecha)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if camion_id is not None:
        incidencias = Incidencia.objects.filter(camion=camion_id)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if motor_id is not None:
        incidencias = Incidencia.objects.filter(motor=motor_id)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if fecha is not None:
        incidencias = Incidencia.objects.filter(fecha_incidencia__date=fecha)
        serializer = IncidenciaSerializer(incidencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    incidencias = Incidencia.objects.all()
    serializer = IncidenciaSerializer(incidencias, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)









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
    incidents = Incidencia.objects.all()
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

@api_view(['PATCH'])
def edit_password(request):
    id_usuario = request.data["mechanic_id"]
    old_password = request.data["oldPassword"]
    new_password = request.data["newPassword"]
    valid_new_password = request.data["validNewPassword"]
    serializer = UsuarioSerializer(data=request.data)
    
    if serializer.is_valid():
        print(f"Serializer data: {serializer.validated_data}")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    print(f"Serializer errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
def creacion_motor(request):
    print(request.data)
    serializer = MotorSerializer(data=request.data)
    if serializer.is_valid():
        print(f"Serializer data: {serializer.validated_data}")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(f"Serializer errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def creacion_camion(request):
    print(request.data)
    serializer = CamionSerializer(data=request.data)
    if serializer.is_valid():
        print(f"Serializer data: {serializer.validated_data}")
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(f"Serializer errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET'])
def getAllCamiones(request):
    serializer = CamionSerializer
    camiones = Camion.objects.all()
    if camiones is not None:
        serializer = CamionSerializer(camiones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No hay camiones creados'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAllMotores(request):
    serializer = MotorSerializer
    motores = Motor.objects.all()
    if motores is not None:
        serializer = MotorSerializer(motores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No hay motores creados'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAllAsignaciones(request):
    serializer = AsignacionMotorCamionSerializer(data=request.data)
    asignaciones = AsignacionMotorCamion.objects.all()
    if asignaciones is not None:
        serializer = AsignacionMotorCamionSerializer(asignaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No hay motores creados'}, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['POST'])
#def asignacionMotorCamion(request):
 #   serializer = AsignacionMotorCamionSerializer(data=request.data)
  #  if serializer.is_valid():
    #    print(f"Serializer data: {serializer.validated_data}")
   #     serializer.save()
    #    return Response(serializer.data, status=status.HTTP_201_CREATED)
    #print(f"Serializer errors: {serializer.errors}")
    #return Response(serializer.errors, status=status.   HTTP_400_BAD_REQUEST)  
