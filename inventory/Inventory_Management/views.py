# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from Inventory_Management import serializers
from Inventory_Management import models
from django.http import HttpResponse

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = Equipment.objects.all()
#    serializer_class = EquipSerializer
##    def get_queryset(self):
##        queryset = Computer.objects.all()
##        return queryset
#
#class ComputerViewSet(viewsets.ModelViewSet):
#    queryset = Computer.objects.all()
#    serializer_class = ComputerSerializer
#
#class Custom(viewsets.ModelViewSet):
#    queryset = Computer.objects.all()
#    serializer_class = EquipSerializer
##    def get_queryset(self, value):
##        queryset = Computer.objects.all()
##        serializer_class = ComputerSerializer
##        return queryset

class VManufacturer(generics.ListAPIView):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.SManufacturer
    def get_queryset(self):
        Mname = self.kwargs['Mname']
        return Manufacturer.objects.filter(name=Mname)

class VVendor (viewsets.ModelViewSet):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.SVendor

class VLocation (viewsets.ModelViewSet):
    queryset=models.Location.objects.all()
    serializer_class = serializers.SLocation

class VModelNumber (viewsets.ModelViewSet):
    queryset=models.ModelNumber.objects.all()
    serializer_class = serializers.SModelNumber

class VMemory (viewsets.ModelViewSet):
    queryset=models.Memory.objects.all()
    serializer_class = serializers.SMemory

class VHardDrive (viewsets.ModelViewSet):
    queryset=models.HardDrive.objects.all()
    serializer_class = serializers.SHardDrive

#class (viewsets.ModelViewSet):
#    queryset=models..objects.all()
#    serializer_class = serializers.