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
from inf236backend.views import MotorViewSet, CamionViewSet, AsignacionMotorCamionViewSet, handle_incident, login_view, search_incidents
from inf236backend.views import search_asign, submit_incident, getAllIncidents, search_incidents, edit_incident

router = DefaultRouter()
router.register(r'motor',MotorViewSet)
router.register(r'camion',CamionViewSet)
router.register(r'asignacion',AsignacionMotorCamionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
    #path('api/incidents/', handle_incident, name='handle_incident'), #Path de Vista, linea de prueba
    #path('api/allincidents/', getAllIncidents, name='getAllIncidents'), #Path de Vista, linea de prueba
    #path('api/search/', search_incidents, name='search_incidents'),

    path('api/login/', login_view, name='login_view'),
    path('api/asigns/', search_asign, name='search_asign'),
    path('api/incidents/submit/', submit_incident, name='submit_incident'),
    path('api/incidents/all/', getAllIncidents, name='getAllIncidents'),
    path('api/incidents/', search_incidents, name='search_incidents'),
    path('api/incidents/editing/', edit_incident, name='edit_incident')
]
