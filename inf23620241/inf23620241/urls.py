"""
URL configuration for inf23620241 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inf236backend.views import MotorViewSet, SistemaViewSet, ComponenteViewSet, CamionViewSet, AsignacionMotorCamionViewSet, UsuarioViewSet, IncidenciaViewSet, AntecedenteViewSet
from inf236backend.views import login, filtrar_incidencias

from inf236backend.views import creacion_motor, creacion_camion, getAllCamiones, getAllMotores, getAllAsignaciones, handle_incident, search_incidents, search_asign, submit_incident, getAllIncidents, search_incidents, edit_incident, edit_password, creacion_usuario, getAllTrucks

router = DefaultRouter()
router.register(r'motor',MotorViewSet)
router.register(r'sistema',SistemaViewSet)
router.register(r'componente',ComponenteViewSet)
router.register(r'camion',CamionViewSet)
router.register(r'asignacion',AsignacionMotorCamionViewSet)
router.register(r'usuario',UsuarioViewSet)
router.register(r'incidencia',IncidenciaViewSet)
router.register(r'antecedente', AntecedenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
    #path('api/incidents/', handle_incident, name='handle_incident'), #Path de Vista, linea de prueba
    #path('api/allincidents/', getAllIncidents, name='getAllIncidents'), #Path de Vista, linea de prueba
    #path('api/search/', search_incidents, name='search_incidents'),

    path('api/asigns/', search_asign, name='search_asign'),
    path('api/incidents/submit/', submit_incident, name='submit_incident'),
    path('api/incidents/all/', getAllIncidents, name='getAllIncidents'),
    path('api/incidents/', search_incidents, name='search_incidents'),
    path('api/incidents/edit/', edit_incident, name='edit_incident'),
    path('api/login/edit/', edit_password, name='edit_password'),
    path('api/camiones/', getAllCamiones, name='get_all_camiones'),
    path('api/usuario/', creacion_usuario, name='creacion_usuario'),


    ######## Work with original BBDD #####
    path('api/sesion/', login, name='login'),
    path('api/incidencias/', filtrar_incidencias, name='filtrar_incidencias'),
    path('api/motor/create', creacion_motor, name='creacion_motor'),
    path('api/camion/create', creacion_camion, name='creacion_camion'),
    path('api/camion/all', getAllCamiones, name='getAllCamiones'),
    path('api/motor/all', getAllMotores, name='getAllMotores'),
    path('api/asignacion/all', getAllAsignaciones, name='getAllAsignaciones'),
    path('api/camiones/', getAllTrucks, name= 'get_all_trucks'),
    #path('api/antecedentes/submit/', submit_antecedente, name='submitantecedente'),

]

