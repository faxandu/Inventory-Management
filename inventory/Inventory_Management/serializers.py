#I prefix all classes with a captial S so signify that they are serializer classes, while
#there is no techinical reason for this, it helps to avoid ambiguity in general talks about
#the system

from rest_framework import serializers
from Inventory_Management import models

#these are just tables that are needed on there own to avoid duplicate entires(and thus save 
#space) but are used in other tables as forigen keys
class SLocation(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('building', 'room')

class SManufacturer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('name',)

class SVendor(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('name',)

#depsite being called number, it holds chars
class SModelNumber(serializers.ModelSerializer):
    class Meta:
        model = models.ModelNumber
        fields = ('number',)

class SService(serializers.ModelSerializer):
    class Meta:
        model = models.Service_contract
        fields = ('service',)

class SPort(serializers.ModelSerializer):
    class Meta:
        model = models.Port
        fields = ('name', 'type_of_port')

#this is the root type for all types, there is little usable need for haveing a serializer
# for it, but included anyways so we have a means of returning all entries of the database
class SEquipment(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate')

#the rest of these are at points down the inheritence chain, starting with Equipment
#unit is full sysems, like a computer, switch, router, so on. for consistancy, the order
#of the fields are kept in order, starting with the parent class fields.
class SUnit(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

#componet is smaller parts, such as ram
class SComponent(serializers.ModelSerializer):
    class Meta:
        model = models.Component
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

#the following is objects from type componet, there are 7 of these classes

class SHardDrive(serializers.ModelSerializer):
    class Meta:
        model = models.HardDrive
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'size')

class SMother_board(serializers.ModelSerializer):
    class Meta:
        model = models.Mother_board
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SCentral_processing_unit(serializers.ModelSerializer):
    class Meta:
        model = models.Central_processing_unit
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'clock_speed')

class SOptical_drive(serializers.ModelSerializer):
    class Meta:
        model = models.Optical_drive
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SOperating_system(serializers.ModelSerializer):
    class Meta:
        model = models.Operating_system
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SPower_supply_unit(serializers.ModelSerializer):
    class Meta:
        model = models.Power_supply_unit
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SMemory(serializers.ModelSerializer):
    class Meta:
        model = models.Memory
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'mem_type', 'size_in_megs', 'type_of_ram')

#the following 2 are derived from Memory
class SRam(serializers.ModelSerializer):
    class Meta:
        model = models.Ram
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'mem_type', 'size_in_megs', 'type_of_ram')

class SFlash_Memory(serializers.ModelSerializer):
    class Meta:
        model = models.Flash_Memory
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'mem_type', 'size_in_megs', 'type_of_ram')

#these are inherited from type unit, there are 2 of them
class SComputer(serializers.ModelSerializer):
    class Meta:
        model = models.Computer
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'cpu', 'optical_drive', 'hdd', 'ram', 'psu', 'number_of_mem_sticks', 'IS_tag')

class SRouter(serializers.ModelSerializer):
    class Meta:
        model = models.Router
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'IS_tag', 'ports', 'number_of_mem_sticks', 'service_contract', 'ram', 'flash')

#from router, we have 2 more

class SFirewall(serializers.ModelSerializer):
    class Meta:
        model = models.Firewall
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'IS_tag', 'ports', 'number_of_mem_sticks', 'service_contract', 'ram', 'flash', 'expansion_slot')

class SSwitch(serializers.ModelSerializer):
    class Meta:
        model = models.Switch
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'IS_tag', 'ports', 'number_of_mem_sticks', 'service_contract', 'ram', 'flash', 'expansion_slot')