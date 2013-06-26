#from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics#generics is here for if we need generics.ListAPIView
from Inventory_Management import serializers
from Inventory_Management import models

#core types
class VLocation(viewsets.ModelViewSet):
    queryset=models.Location.objects.all()
    serializer_class = serializers.SLocation

class VManufacturer(viewsets.ModelViewSet):
    queryset=models.Manufacturer.objects.all()
    serializer_class = serializers.SManufacturer

class VVendor(viewsets.ModelViewSet):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.SVendor

class VModelNumber(viewsets.ModelViewSet):
    queryset=models.ModelNumber.objects.all()
    serializer_class = serializers.SModelNumber

class VService(viewsets.ModelViewSet):
    queryset=models.Service.objects.all()
    serializer_class = serializers.SService

#main inherited type
class VEquipment(viewsets.ModelViewSet):
    queryset=models.Equipment.objects.all()
    serializer_class = serializers.SEquipment

#the two main inherited types
class VUnit(viewsets.ModelViewSet):
    queryset=models.Unit.objects.all()
    serializer_class = serializers.SUnit

class VComponent(viewsets.ModelViewSet):
    queryset=models.Component.objects.all()
    serializer_class = serializers.SComponent

#the componet types, there are 7 of these
class VMemory(viewsets.ModelViewSet):
    queryset=models.Memory.objects.all()
    serializer_class = serializers.SMemory

class VHardDrive(viewsets.ModelViewSet):
    queryset=models.HardDrive.objects.all()
    serializer_class = serializers.SHardDrive

class VMother_board(viewsets.ModelViewSet):
    queryset=models.Mother_board.objects.all()
    serializer_class = serializers.SMother_board

class VCentral_processing_unit(viewsets.ModelViewSet):
    queryset=models.Central_processing_unit.objects.all()
    serializer_class = serializers.SCentral_processing_unit

class VOptical_drive(viewsets.ModelViewSet):
    queryset=models.Optical_drive.objects.all()
    serializer_class = serializers.SOptical_drive

class VOperating_system(viewsets.ModelViewSet):
    queryset=models.Operating_system.objects.all()
    serializer_class = serializers.SOperating_system

class VPower_supply_unit(viewsets.ModelViewSet):
    queryset=models.Power_supply_unit.objects.all()
    serializer_class = serializers.SPower_supply_unit

#these are of type unit
class VRouter(viewsets.ModelViewSet):
    queryset=models.Router.objects.all()
    serializer_class = serializers.SRouter

class VComputer(viewsets.ModelViewSet):
    queryset=models.Computer.objects.all()
    serializer_class = serializers.SComputer