from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rides.models import Rides
from rest_framework.authentication import TokenAuthentication
from rides.serializers import Rideserializer
from rest_framework.permissions import IsAuthenticated
from rides.serializers import Userserializer
from django.contrib.auth.models import User


# Create your views here.
class Rideview(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Rides.objects.all()
    serializer_class=Rideserializer


class Registerview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer