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

class VService_contract(viewsets.ModelViewSet):
    queryset=models.Service_contract.objects.all()
    serializer_class = serializers.SService

class VPort(viewsets.ModelViewSet):
    queryset=models.Port.objects.all()
    serializer_class = serializers.SPort

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

class VMemory(viewsets.ModelViewSet):
    queryset=models.Memory.objects.all()
    serializer_class = serializers.SMemory

#these are derived from Memory
class VRam(viewsets.ModelViewSet):
    queryset=models.Ram.objects.all()
    serializer_class = serializers.SRam

class VFlash_Memory(viewsets.ModelViewSet):
    queryset=models.Flash_Memory.objects.all()
    serializer_class = serializers.SFlash_Memory

#these are of type unit
class VComputer(viewsets.ModelViewSet):
    queryset=models.Computer.objects.all()
    serializer_class = serializers.SComputer

class VRouter(viewsets.ModelViewSet):
    queryset=models.Router.objects.all()
    serializer_class = serializers.SRouter

#these are from type router
class VSwitch(viewsets.ModelViewSet):
    queryset=models.Switch.objects.all()
    serializer_class = serializers.SSwitch

class VFirewall(viewsets.ModelViewSet):
    queryset=models.Firewall.objects.all()
    serializer_class = serializers.SFirewall