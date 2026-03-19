
from rest_framework import serializers
from rides.models import Rides
from django.contrib.auth.models import User

class Rideserializer(serializers.ModelSerializer):
    class Meta:
        model=Rides
        fields="__all__"

class Userserializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


    def create(self,validated_data):
       user=User.objects.create_user(**validated_data)
       return user