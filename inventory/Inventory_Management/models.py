from django.db import models
import datetime
from django.utils import timezone
 
class Equipment(models.Model):
    '''
        Base model for Unit and Component
    '''
    manufacturer = models.ForeignKey('Manufacturer')
    model_num = models.ForeignKey('ModelNumber', blank = True, null = True) #---------------__FLAG
    serial_num = models.CharField(max_length = 35, unique = True, blank= True,null = True) 
    purchaseDate = models.DateField()

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
        }

class Unit(Equipment):
    '''
        Computer, Router, Switch, etc.
    '''
    location = models.ForeignKey('Location', blank=False)

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
        }


class Component(Equipment):
    '''
        For components such as RAM, CPU, etc.
    '''
    location = models.ForeignKey('Location', blank=True, null=True)
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
        }

class Location(models.Model):
    '''
        Docstring needed
    '''
    building = models.CharField(max_length=2)
    room = models.CharField(max_length=4)

    def __unicode__(self):
        return unicode(self.building + ' ' + self.room)
        
    def to_dict(self):
        return {
            'id':self.id,
            'room':self.room,
            'building':self.building
        }


class Manufacturer(models.Model):
    '''
        Docstring needed
    '''
    name = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    def to_dict(self):
        return {
            'id':self.id,
            'name':unicode(self.name)
        }

class Vendor(models.Model):
    '''
        Seller
    '''
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    def to_dict(self):
        return {
            'id':self.id,
            'name':unicode(self.name)
        }

class ModelNumber(models.Model):
    number = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.number)
        
    def to_dict(self):
        return {
            'id':self.id,
            'number':unicode(self.number)
        }


class Memory(Component):
    CHOICES = (
        ('RAM', 'RAM'),
        ('Flash', 'Flash'),
    )
    mem_type = models.CharField(max_length=10, choices=CHOICES)
    size_in_megs = models.IntegerField()
    type_of_ram = models.CharField(max_length=10, blank=True, null=True)
    def __unicode__(self):
        return unicode(str(self.manufacturer) + " " + str(self.size_in_megs) + " " + str(self.mem_type))

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'mem_type': unicode(self.mem_type),
            'size_in_megs': unicode(self.size_in_megs),
            'type_of_ram': unicode(self.type_of_ram),
        }


class Ram(Memory): #pass

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'mem_type': unicode(self.mem_type),
            'size_in_megs': unicode(self.size_in_megs),
            'type_of_ram': unicode(self.type_of_ram),
        }


class Flash_Memory(Memory): #pass

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'mem_type': unicode(self.mem_type),
            'size_in_megs': unicode(self.size_in_megs),
            'type_of_ram': unicode(self.type_of_ram),
        }


class HardDrive(Component):
    size = models.IntegerField()

    def __unicode__(self):
            return unicode(str(self.manufacturer) + " " + str(self.size))
            
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'size': unicode(self.size),
        }

class Mother_board(Component):# pass

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
        }

class Central_processing_unit(Component):
    clock_speed = models.FloatField()
    def __unicode__(self):
        return unicode(str(self.manufacturer) +  " " + str(self.clock_speed))
        
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'clock_speed': unicode(self.clock_speed),
        }

class Optical_drive(Component): #pass

    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
        }

class Operating_system(Component):
    name = models.CharField(max_length = 11, blank=True)
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'name': unicode(self.name),
        }

    def __unicode__(self):
        return unicode(self.name)

class Power_supply_unit(Component):
    power_rating = models.CharField(max_length = 8, blank=True)
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'power_rating': unicode(self.power_rating),
        }


class Service_contract(models.Model):
    service_contract = models.TextField() 
    
    def to_dict(self):
        return {
            'id':self.id,
            'service_contract':unicode(self.service_contract)
        }

class Router(Unit):
    IS_tag = models.IntegerField(blank=True,null = True)
    ports = models.ForeignKey('Port') 
    number_of_mem_sticks = models.IntegerField()
    service_contract = models.ForeignKey('Service_contract')
    ram = models.ForeignKey('Ram')
    flash = models.ForeignKey('Flash_Memory', blank=True,null = True) 
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'IS_tag': unicode(self.IS_tag),
            'ports': self.ports.to_dict(),
            'number_of_mem_sticks': unicode(self.number_of_mem_sticks),
            'service_contract': self.service_contract.to_dict(),
            'ram': self.ram.to_dict(),
            'flash': self.flash.to_dict(),
        }

class Port(models.Model): 
    name = models.IntegerField()
    type_of_port = models.CharField(max_length = 10, blank=True, null=True)
    
    def to_dict(self):
        return {
            'id':self.id,
            'name':unicode(self.name),
            'type_of_port':unicode(self.type_of_port)
        }


class Firewall(Router): 
    expansion_slot = models.TextField(blank=True,null=True)
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'IS_tag': unicode(self.IS_tag),
            'ports': self.ports.to_dict(),
            'number_of_mem_sticks': unicode(self.number_of_mem_sticks),
            'service_contract': self.service_contract.to_dict(),
            'ram': self.ram.to_dict(),
            'flash': self.flash.to_dict(),
            'expansion_slot': unicode(self.expansion_slot),
        }

class Switch(Router): 
    expansion_slot = models.TextField(blank=True,null=True) 
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'IS_tag': unicode(self.IS_tag),
            'ports': self.ports.to_dict(),
            'number_of_mem_sticks': unicode(self.number_of_mem_sticks),
            'service_contract': self.service_contract.to_dict(),
            'ram': self.ram.to_dict(),
            'flash': self.flash.to_dict(),
            'expansion_slot': unicode(self.expansion_slot),
        }

class Computer(Unit): 
    cpu = models.ForeignKey('Central_processing_unit')
    optical_drive = models.ForeignKey('Optical_drive')
    hdd = models.ForeignKey('HardDrive')
    ram = models.ForeignKey('Ram')
    psu = models.ForeignKey('Power_supply_unit')
    number_of_mem_sticks = models.IntegerField()
    IS_tag = models.IntegerField()
    
    def to_dict(self):
        if not self.model_num:
            model_num = ''
        else:
            model_num = self.model_num.to_dict()
        return {
            'id':self.id,
            'manufacturer':self.manufacturer.to_dict(),
            'model_num':self.model_num.to_dict(),
            'serial_num': unicode(self.serial_num),
            'purchaseDate': unicode(self.purchaseDate),
            'location': self.location.to_dict(),
            'cpu': self.cpu.to_dict(),
            'optical_drive': self.optical_drive.to_dict(),
            'hdd': self.hdd.to_dict(),
            'ram': self.ram.to_dict(),
            'psu': self.psu.to_dict(),
            'number_of_mem_sticks': unicode(self.number_of_mem_sticks),
            'IS_tag': unicode(self.IS_tag),
        }
