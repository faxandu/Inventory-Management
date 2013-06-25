from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

#number is implied
#class Equip_Type(models.Model):
#	eType = models.CharField(max_length=20, unique=True)
#
#	def __unicode__(self):
#		return unicode(self.eType)
#
#class Location(models.Model):
#	room = models.CharField(max_length=4)
#	building = models.CharField(max_length=2)
#	def __unicode__(self):
#		return unicode(self.building + self.room)
#
#class Equipment(models.Model):
#	model_num = models.IntegerField()
#	serial_num = models.IntegerField()
#	equip_type = models.ForeignKey(Equip_Type)
#	location = models.ForeignKey(Location)
#	description = models.TextField()
#	now = models.DateTimeField(auto_now_add=True)
#
#	def __unicode__(self):
#		return unicode(self.description)
#
#
#class Computer(Equipment):
#	ram = models.IntegerField()
#	max_ram = models.IntegerField()
#
#--------------------------------------------------------

class Manufacturer(models.Model):
    '''
    Docstring needed
    '''
    name = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return unicode(self.name)

class Vendor(models.Model):
    '''
    Seller of Units
    '''
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return unicode(self.name)

class Location(models.Model):
    '''
    Docstring needed
    '''
    building = models.CharField(max_length=2)
    room = models.CharField(max_length=4)

    def __unicode__(self):
        return unicode(self.building + self.room)

class ModelNumber(models.Model):
    number = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.number)

class Equipment(models.Model):
    '''
    Base model for Unit and Component
    '''
    
class Component(Equipment):
#	CompontetManufacturer = ForienKey(Manufacturer)
    '''
    For components such as RAM, CPU, etc.
    '''
    pass

class Memory(Component):
    CHOICES = (
        ('RAM', 'RAM'),
        ('Flash', 'Flash'),
    )
    mem_type = models.CharField(max_length=10,
                                choices=CHOICES)
    size_in_megs = models.IntegerField()

class HardDrive(Component):
    size = models.IntegerField()
    def __unicode__(self):
            return unicode(str(self.manufacturer) + " " + str(self.size))

class Mother_board(Component): pass

class Central_processing_unit(Component):
    clock_speed = models.FloatField()
    def __unicode__(self):
        return unicode(str(self.manufacturer) + " " + str(self.clock_speed))

class Optical_drive(Component): pass

class Operating_system(Component):
    name = models.CharField(max_length = 11, blank=True)
    def __unicode__(self):
        return unicode(self.name)

class Power_supply_unit(Component):
    power_rating = models.CharField(max_length = 8, blank=True)

class Unit(Equipment):
    '''
    Computer, Router, Switch, etc.
    '''
    manufacturer = models.ForeignKey(Manufacturer)
    model_num = models.ForeignKey(ModelNumber)
    serial_num = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    location = models.ForeignKey('Location')
    vendor = models.ForeignKey(Vendor, null=True)
    
class Router(Unit):
    IS_tag = models.IntegerField()
    ports = models.IntegerField()

class Computer(Unit): pass

