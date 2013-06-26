from django.db import models
import datetime
from django.utils import timezone


 
class Equipment(models.Model):
    '''
        Base model for Unit and Component
    '''
    manufacturer = models.ForeignKey('Manufacturer')
    model_num = models.ForeignKey('ModelNumber')
    serial_num = models.CharField(max_length = 35, unique = True)
    purchaseDate = models.DateField()


class Unit(Equipment):
    '''
        Computer, Router, Switch, etc.
    '''
    location = models.ForeignKey('Location', blank=False)


class Component(Equipment):
    '''
        For components such as RAM, CPU, etc.
    '''
    location = models.ForeignKey('Location', blank=True, null=True)


class Location(models.Model):
    '''
        Docstring needed
    '''
    building = models.CharField(max_length=2)
    room = models.CharField(max_length=4)

    def __unicode__(self):
        return unicode(self.building + self.room)


class Manufacturer(models.Model):
    '''
        Docstring needed
    '''
    name = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return unicode(self.name)


class Vendor(models.Model):
    '''
        Seller
    '''
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return unicode(self.name)


class ModelNumber(models.Model):
    number = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.number)


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


class Ram(Memory): pass


class Flash_Memory(Memory): pass


class HardDrive(Component):
    size = models.IntegerField()

    def __unicode__(self):
            return unicode(str(self.manufacturer) + " " + str(self.size))

class Mother_board(Component): pass

class Central_processing_unit(Component):
    clock_speed = models.FloatField()
    def __unicode__(self):
        return unicode(str(self.manufacturer) +  " " + str(self.clock_speed))

class Optical_drive(Component): pass

class Operating_system(Component):
    name = models.CharField(max_length = 11, blank=True)

    def __unicode__(self):
        return unicode(self.name)

class Power_supply_unit(Component):
    power_rating = models.CharField(max_length = 8, blank=True)

class Service(models.Model):
    service = models.TextField()

class Router(Unit):
    IS_tag = models.IntegerField()
    ports = models.IntegerField()
    number_of_mem_sticks = models.IntegerField()
    service = models.ForeignKey('Service')
    ram = models.ForeignKey('Ram')
    flash = models.ForeignKey('Flash_Memory')

    #def __unicode__(self):
       # return unicode(self.name)
class Computer(Unit): 
    cpu = models.ForeignKey('Central_processing_unit')
    optical_drive = models.ForeignKey('Optical_drive')
    hdd = models.ForeignKey('HardDrive')
    ram = models.ForeignKey('Ram')
    psu = models.ForeignKey('Power_supply_unit')
    number_of_mem_sticks = models.IntegerField()
    IS_tag = models.IntegerField()
        
   # def __unicode__(self):
      #  return unicode(self.name)