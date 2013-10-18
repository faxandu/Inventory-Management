'''
Explinataion of database

for a breakdown of each field, see the bottom of the file, likewise for the functions attached to the classes

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

#this object is used for the Modelnum table as the source for the choices in stype
model_type = (
    ('HD','Hard_drive'),
    ('MB','Mother_board'),
    ('MT','Memory'),
    ('OS','Operating_system'),
    ('CP','CPU'),
    ('FT','Flash_type'),
    ('OD','Optical_drive'),
    )
    
class Modelnum(models.Model):
    model_number = models.CharField(max_length = 25, unique = True)
    model_type = models.CharField(max_length = 20, choices = model_type)
    
    def __unicode__(self):
        return unicode(self.model_number)

    def to_dict(self):
        return {
            'name': self.model_number,
        }

#class Memory_type(models.model):
#    name = models.CharField(max_length = 25, unique = True)

#class Manufacturer(models.Model):
#    name = models.CharField(max_length = 25, unique = True)

''' removed to reduce table useage
class Hard_drive_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Mother_board_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Operating_system_name(models.model):
    name = models.CharField(max_length = 25, unique = True)

class CPU_model(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Flash_type(models.Model):
    name = models.CharField(max_length = 25, unique = True)

class Optical_drive_model(models.Model)
    name = models.CharField(max_length = 25, unique = True)
'''

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
    acquisition_date = models.DateField(blank = True, null = True)
    #service_tag = models.CharField(max_length = 35, blank = True, null = True)
    IS = models.CharField(max_length = 35, blank = True, unique = False, null = True)
    machine_name = models.CharField(max_length = 100, unique = False, blank = True, null = True)
    in_use = models.BooleanField()
    location = models.TextField(blank = True, null = True)

    def to_dict(self):
        HD = self.hard_drive_set.all()
        HDD = [i.list_view() for i in HD]
        MB = self.motherboard_set.all()
        MBD = [i.list_view() for i in MB]
        CP = self.central_processing_unit_set.all()
        CPD = [i.list_view() for i in CP]
        PS = self.power_supply_unit_set.all()
        PSD = [i.list_view() for i in PS]
        OD = self.optical_drive_set.all()
        ODD = [i.list_view() for i in OD]
        RM = self.ram_set.all()
        RMD = [i.list_view() for i in RM]
        OS = self.operating_system_set.all()
        OSD = [i.list_view() for i in OS]
        FM = self.flash_memory_set.all()
        FMD = [i.list_view() for i in FM]
        SC = self.service_contract_set.all()
        SCD = [i.list_view() for i in SC]
        EC = self.expansion_card_set.all()
        ECD = [i.list_view() for i in EC]
        
        return {
            'id' : self.id,
            'acquisition_date' : unicode(self.acquisition_date),
            'IS' : unicode(self.IS),
            'machine_name' : unicode(self.machine_name),
            'in_use' : self.in_use,
            'location' : unicode(self.location),
            'Hard_drive' : HDD, #this is the line to look at for getting the list in the list
            'Motherboard' : MBD,
            'Central_processing_unit' : CPD,
            'Power_supply_unit' : PSD,
            'Optical_drive_set' : ODD,
            'RAM' : RMD,
            'Operating_system' : OSD,
            'Flash_memory' : FMD,
            'Service_contract' : SCD,
            'Expansion_card' : ECD,
        }
    
    def __unicode__(self):
        return self.machine_name
        
    def part_view(self):
        return {
            'machine_name':self.machine_name,
        }

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
likewise,
pending -- having them all inherit from a common type makes for an easy API call
'''

#acquisition_date = models.DateField()

class Hard_drive(models.Model):
    total_GB = models.IntegerField()
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')
    #interface type, add later perhaps
    
    def to_dict(self):
        return {
            'id' : self.id,
            'total_GB' : self.total_GB,
            'model' : self.model.to_dict(),
            'location' : self.location.part_view(),
        }
    
    def list_view(self):
        return {
            'total_GB' : self.total_GB,
            'model' : self.model.to_dict(),
        }
        
    def __unicode__(self):
        return unicode(self.model)

class Motherboard(models.Model):
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
        }
    
    def __unicode__(self):
        return unicode(self.model)

class Central_processing_unit(models.Model):
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
        }
    
    def __unicode__(self):
        return unicode(self.model)

class Power_supply_unit(models.Model):
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
        }
    
    def __unicode__(self):
        return unicode(self.model)

class Optical_drive(models.Model):
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
        }
    
    def __unicode__(self):
        return unicode(self.model)

class RAM(models.Model):
    model = models.ForeignKey('Modelnum')
    #manufacturer = models.ForeignKey('Manufacturer')
    size_in_gigs = models.IntegerField()
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'size_in_gigs' : self.size_in_gigs,
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
            'size_in_gigs' : self.size_in_gigs,
        }
    
    def __unicode__(self):
        return unicode(self.model)

class Operating_system(models.Model):
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
        }
    
    def __unicode__(self):
        return unicode(self.model)

class Flash_memory(models.Model):
    model = models.ForeignKey('Modelnum')
    size_in_megs = models.IntegerField()
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'model' : self.model.to_dict(),
            'size_in_megs' : self.size_in_megs,
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'model' : self.model.to_dict(),
            'size_in_megs' : self.size_in_megs,
        }
    
    def __unicode__(self):
        return unicode(self.model)

class Service_contract(models.Model):
    name = models.CharField(max_length = 25, unique = True)
    location = models.ForeignKey('Equipment')
    expire_date = models.DateField()
    additional_notes = models.TextField()

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'location' : self.location.part_view(),
            'expire_date' : unicode(self.expire_date),
            'additional_notes' : self.additional_notes,
        }
        
    def list_view(self):
        return {
            'name' : self.name,
            'expire_date' : unicode(self.expire_date),
            'additional_notes' : self.additional_notes,
        }
    
    def __unicode__(self):
        unicode(self.name)

class Expansion_card(models.Model):
    description = models.TextField()
    location = models.ForeignKey('Equipment')

    def to_dict(self):
        return {
            'id' : self.id,
            'description' : self.description,
            'location' : self.location.part_view(),
        }
        
    def list_view(self):
        return {
            'description' : self.description,
        }

    def __unicode__(self):
        return unicode(self.description)

'''
breakdown of a database table:

for reference, we will use the hard drive field for reference by line

class Hard_drive(models.Model):
    size_in_gigs = models.IntegerField()
    model = models.ForeignKey('Modelnum')
    location = models.ForeignKey('Equipment')
    
breaking down the fields

class Hard_drive(models.Model):

tables in Django are represented as classes, which inherits from Model (hence the import at the top for models)
due to how python deals with importing code, we reference it by file_name.class_name . Hard_drive is just the table
name, and class is, well, its a class.

    size_in_gigs = models.IntegerField()
    
don't forget indentation, we still adhear to python syntax(this project uses 4 spaces per indent). whats on the left
of the assignement operator is just a variable name, about what you would expect from any language. on the right
we once again take something from the models file, in this case an IntergerField. this is just an object that we use
to represent -as you have guessed- Integers in the database. there's a long list of what can be used here and most 
are very self descriptive in the name, such as Floatfield, CharField, etc...

    model = models.ForeignKey('Modelnum')
    
ForeignKey is how we make relations in the database, what this is saying is that the field is pointing to another table.
in this case, we are specifying the Modelnum table. what it actualy stores in the database is the ID field of that table.
(if not known at this time, all tables will automaticaly add the ID field for its primary key, if one is not specified)

making note of one other field here

class Computer(Equipment): pass

what this means is its inheriting from equipment so it takes on all of its fields, and pass is a python syntax
saying that there is no mode code to add on to the class, just finish it.
'''
