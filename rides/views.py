from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rides.models import Rides
from rides.serializers import Rideserializer
from rest_framework.permissions import IsAuthenticated
from rides.serializers import Userserializer
from django.contrib.auth.models import User



class Rideview(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Rides.objects.all()
    serializer_class=Rideserializer
    @action(detail=True,methods=['POST'])
    def ridestatusupdate(self, request, pk):
        ride = Rides.objects.get(id=pk)
        new_status=request.data.get("status")
        if new_status in ['STARTED', 'COMPLETED', 'CANCELLED']:
            if ride.status != 'COMPLETED':
                ride.status=new_status
                ride.save()
                return Response({"message": "Ride update successfully"})
            else:
                return Response({"error": "Ride already completed"})
        else:
            return Response({"error": "Invalid status"})
    @action(detail=True,methods=['POST'])
    def updatelocation(self,request,pk):
        ride=Rides.objects.get(id=pk)
        lat=request.data.get("latitude")
        lon=request.data.get("longitude")
        if lat and lon:
            ride.latitude=lat
            ride.longitude=lon
            ride.save()
            return Response({"message": "Location updated"})
        else:
            return Response({"error": "Latitude and Longitude required"})

    @action(detail=True, methods=['post'])
    def matchdriver(self, request, pk):
        ride=Rides.objects.get(id=pk)
        drivers=["Arun", "Rahul", "amal"]
        ride.driver=drivers[0]
        ride.save()
        return Response({"message": "Driver assigned"})

    @action(detail=True, methods=['post'])
    def acceptride(self, request, pk):
        ride=Rides.objects.get(id=pk)
        if ride.driver:
            ride.status="STARTED"
            ride.save()
            return Response({"message": "Ride started"})
        return Response({"error": "No driver assigned"})



class Registerview(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserializer