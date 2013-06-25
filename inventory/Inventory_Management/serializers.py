#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Inventory_Management import models

#class EquipSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Equipment
#        fields = ('description', 'model_num', 'serial_num', 'equip_type', 'location', 'now',)
#
#class ComputerSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Computer
#        fields = ('description', 'model_num', 'serial_num', 'equip_type', 'location', 'now', 'ram', 'max_ram',)

class SManufacturer (serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('name',)

class SVendor (serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('name',)

class SLocation (serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('building', 'room',)


class SModelNumber (serializers.ModelSerializer):
    class Meta:
        model = models.ModelNumber
        fields = ('number',)

class SMemory (serializers.ModelSerializer):
    class Meta:
        model = models.Memory
        fields = ('mem_type', 'size_in_megs',)

class SHardDrive (serializers.ModelSerializer):
    class Meta:
        model = models.HardDrive
        fields = ('size',)
#class (serializers.ModelSerializer):
#    class Meta:
#        model = 
#        fields = ('',)
