from django.shortcuts import render
from rest_framework import viewsets
from .models import Motor
from .serializers import MotorSerializer

# Create your views here.
# Views are in charge of the business logic of the application
# Class ModelViewSet gives us many easy access to CRUD operations (Instead of creating it ourselves)

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer