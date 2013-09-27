'''
Explinataion of database

the database for this project is split up into three catagories for its tables
support/suplemental tables
main/anchor tables
parts/componets tables

the idea for each is a follows: main/anchor tables represent a full unit of some sort, such as a comptuer workstation,
a server on a rack, or whatever we may need to add in the future. parts/componets are anything that is typically attached
to a full machine, such as a hard drive, or motherboard. support/suplemental tables are anything that really -shouldent-
have its own table, but does as data in some of the parts will have a tendancy to repeate themselves, so instead of 
inviting room for uer error from mistypeing informaion, they link to a unique table that won't have that problem.
'''

from django.db import models
import datetime

'''
support/suplemental tables

the following are support/suplemental fields, things that are consistant over many parts, but don't need to be
reiterated over and over in diffrent tables, so are set in there own tables to save space and reduce user error
'''

class Hard_drive_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Mother_board_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Memory_type(models.model):
    name = models.CharField(max_length = 25, unique = True)

class Operating_system_name(models.model):
    name = models.CharField(max_length = 25, unique = True)

class CPU_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Hard_Drive_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Flash_type(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Optical_drive_model(models.Model)
    name = models.CharField(max_length = 25, unique = True)

'''
main/anchor tables

Equipment is anything that can have parts attached to it, such as comptuers or switches(as you see below)
  think of them as anchor points for everything else
by having them all inherit from a core type, it makes API calls for all machines we have simple as we only call one table
it also makes it so we can point to anything that inherits from it, which also simplifies the database so we don't need 
something like "server hdd, computer hdd" for every type.
still inherits from the core type, so it can be pointed to by the other fields. as it's name implies, its for unused parts. 
so the user may enter in a breif description of where its at. (ie, james took it home for testing, its in bill cabinate, etc)
'''

class Equipment(models.Model):
    acquisition_date = models.DateField()
    #service_tag = models.CharField(max_length = 35, blank = True, null = True)
    IS = models.CharField(max_length = 35, blank = True, null = True)
    machine_name = CharField(max_length = 100, unique = False blank = True, null = True)
    in_use = models.BooleanField()
    location = models.TextField()

class Computer(Equipment): pass

class Router(Equipment): pass

class Switch(Equipment): pass

class Firewall(Equipment): pass

class Server(Equipment): pass

#class Unused(Equipment)

'''
the following is what is attached to the object above, they point "upwards" to what they are attached to
more spificaly, they will contain 3 diffrent things at most: common datafields that are unique to indivual parts,
datafields that tend to repeate themselves(the foreignkey fields that are not to equipment) such as OS names,
CPU socket types, stuff that we will want to add on to in the future, but not change once implemented. then the
field that links to something of type equipment, which represents a full machine that it is attached to.
likewise, having them all inherit from a common type makes for an easy API call
'''

#acquisition_date = models.DateField()

class Hard_drive(models.Model):
    size_in_gigs = models.IntegerField()
    model = models.ForeignKey('Hard_drive_model')
    location = models.ForeignKey('Equipment')
    #interface type, add later perhaps

class Mother_board(models.Model):
    model = models.ForeignKey('Mother_board_model')
    location = models.ForeignKey('Equipment')

class Central_processing_unit(models.Model):
    model = models.ForeignKey('CPU_model')
    location = models.ForeignKey('Equipment')

class Power_supply_unit(models.Model):
    model = models.ForeignKey('PSU_model')
    location = models.ForeignKey('Equipment')

class Optical_drive(models.Model):
    model = models.ForeignKey('Optical_drive_model')
    location = models.ForeignKey('Equipment')

class Memory(models.Model):
    memory_type = models.ForeignKey('Memory_type')
    manufacturer = models.ForeignKey('Manufacturer')
    size_in_gigs = models.IntegerField()
    location = models.ForeignKey('Equipment')

class Operating_system(models.Model):
    name = models.ForeignKey('Operating_system_name')
    location = models.ForeignKey('Equipment')

class Flash_Memory(models.Model):
    flash_type = models.ForeignKey('Flash_type')
    size_in_megs = models.IntegerField()
    location = models.ForeignKey('Equipment')
    
    #printers, KVM

class Service_contract(models.Model):
    name = models.CharField(max_length = 25, unique = True)
    
'''
service contract :
number -charfield
link to vendor -foreinkey
experation date -datefield
additional notes -textfield

expantion card:
textfield,

'''
