#I prefix all classes with a captial S so signify that they are serializer classes, while
#there is no techinical reason for this, it helps to avoid ambiguity in general talks about
#the system
'''
===============================
THIS FILE IS LEGACY FROM THE REST FRAMEWORK, IT IS UNUSED
===============================
'''
'''
Understanding what is going on in this file so that it may be used as a reference

definition: serializer
    in the project here, its what converts python code to json

the includes are for both from the rest framework and the projects models. We inherit from the serializer ModelSerializer
    as it was a fast and easy way to convert the information in to our data base in few easily understandable lines

examples: from the location serializer

class SLocation(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'building', 'room')

its standard python syntax, give the class a name, and inherited from ModelSerializer. the requirements from there are
    add another class inside it called Meta, and there are two required fields

    model: you specify what model you want to base the serializer on(hence why we included our model file)
    fields: you specify what field from that model you want to use. for instance, if we ommited the entry 
        'building', when a call were to be made to this serializer, it would return the Location Tables ID, and room,
        but no building as we diden't specify it.

in the bigger tables that inside themselves, hold references to other tables, the class is modifed in a way to get 
    the informaion that is passed through it into an array (when lookin at it in json) and will modify the tables 
    when passed back.

example:

class SUnit(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Unit
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

one thing you can do with the fields in the meta class, is you can pass in a variable instead of just referenceing the 
    model. by setting the fields that are reprensented by other tables to be the same as the serializer for that table,
    we return the same things in that serializer as an array. 
'''

from rest_framework import serializers
from Inventory_Management import models

#these are just tables that are needed on there own to avoid duplicate entires(and thus save 
#space) but are used in other tables as forigen keys
class SLocation(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'building', 'room')

class SManufacturer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('id', 'name',)

class SVendor(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('id', 'name',)

#depsite being called number, it holds chars
class SModelNumber(serializers.ModelSerializer):
    class Meta:
        model = models.ModelNumber
        fields = ('id', 'number',)

class SService_contract(serializers.ModelSerializer):
    class Meta:
        model = models.Service_contract
        fields = ('id', 'service_contract',)

class SPort(serializers.ModelSerializer):
    class Meta:
        model = models.Port
        fields = ('id', 'name', 'type_of_port')

#this is the root type for all types, there is little usable need for haveing a serializer
# for it, but included anyways so we have a means of returning all entries of the database
class SEquipment(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    class Meta:
        model = models.Equipment
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate')

#the rest of these are at points down the inheritence chain, starting with Equipment
#unit is full sysems, like a computer, switch, router, so on. for consistancy, the order
#of the fields are kept in order, starting with the parent class fields.
class SUnit(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Unit
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

#componet is smaller parts, such as ram
class SComponent(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Component
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

#the following is objects from type componet, there are 7 of these classes

class SHardDrive(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.HardDrive
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'size')

class SMother_board(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Mother_board
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SCentral_processing_unit(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Central_processing_unit
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'clock_speed')

class SOptical_drive(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Optical_drive
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SOperating_system(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Operating_system
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SPower_supply_unit(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Power_supply_unit
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location')

class SMemory(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Memory
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'mem_type', 'size_in_megs', 'type_of_ram')

#the following 2 are derived from Memory
class SRam(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Ram
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'mem_type', 'size_in_megs', 'type_of_ram')

class SFlash_Memory(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    class Meta:
        model = models.Flash_Memory
        fields = ('id', 'manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'mem_type', 'size_in_megs', 'type_of_ram')

#these are inherited from type unit, there are 2 of them
class SComputer(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    cpu = SCentral_processing_unit()
    optical_drive = SOptical_drive()
    hdd = SHardDrive()
    ram = SRam()
    psu = SPower_supply_unit()
    class Meta:
        model = models.Computer
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'cpu', 'optical_drive', 'hdd', 'ram', 'psu', 'number_of_mem_sticks', 'IS_tag')

class SRouter(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    ports = SPort()
    service_contract = SService_contract()
    ram = SRam()
    flash = SFlash_Memory
    class Meta:
        model = models.Router
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'IS_tag', 'ports', 'number_of_mem_sticks', 'service_contract', 'ram', 'flash')

#from router, we have 2 more

class SFirewall(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    ports = SPort()
    service_contract = SService_contract()
    ram = SRam()
    flash = SFlash_Memory()
    class Meta:
        model = models.Firewall
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'IS_tag', 'ports', 'number_of_mem_sticks', 'service_contract', 'ram', 'flash', 'expansion_slot')

class SSwitch(serializers.ModelSerializer):
    manufacturer = SManufacturer()
    model_num = SModelNumber()
    location = SLocation()
    ports = SPort()
    service_contract = SService_contract()
    ram = SRam()
    flash = SFlash_Memory()
    class Meta:
        model = models.Switch
        fields = ('manufacturer', 'model_num', 'serial_num', 'purchaseDate', 'location', 'IS_tag', 'ports', 'number_of_mem_sticks', 'service_contract', 'ram', 'flash', 'expansion_slot')
