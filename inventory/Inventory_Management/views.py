#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets, generics#generics is here for if we need generics.ListAPIView
#from Inventory_Management import serializers
from django.http import HttpResponse
from Inventory_Management import models
from django.core import serializers
import json
#for auth
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from django.utils import simplejson

#-------------------most code here is unused/depreciated, scroll to near bottom for relevent code--------------------
'''---------------legacy, uses the rest framework, we have stopped using the rest framework ---------------
Understanding Views: these examples use the rest framework and are obsolete

views are what format the data that we get/pass from the serializers. we inherit from rest_frameworks viewsets for ease
    and import our models as we will need to query them as apart of our view.

example:

class VLocation(viewsets.ModelViewSet):
    queryset=models.Location.objects.all()
    serializer_class = serializers.SLocation

standard python syntax for making a class, inherited from viewsets.ModelViewSet. this has two required fields

    querryset: while in this file we just do evertying in the table, it can be modifed in a way to permit just cetrian 
        elemets based on a query.
    serializer_class: the serializer we use for the view.

'''

'''

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
    serializer_class = serializers.SService_contract

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

'''
'''--------------------------this was a test, ignore------------------------------
@csrf_exempt
@require_http_methods(['POST'])
def login(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.get(user=user).token
        data = {'message': '', 'token': token}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=200)
    else:
        data = {'message': 'Incorrect login'}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=403)

@csrf_exempt
@require_http_methods(['GET'])
def logout(request):
    logout(request)
    return HttpResponse(status=200)
'''
'''----------------------------------------api calls without rest-----------------------------
-------explination of calls to read data-------
this is a break down of each line for the views using location as an example

def VLocation(request):
    request is the object that is passed into the function from the front end, there are things you can do
    with it but are not done in the calls that fetch data. it still needs to be there
    
dictt = models.Location.objects.all()
    dictt is just a shorted name for dictionary(cant use dict, its reserved), and we assign an object that holds
    all instances of the location table. it is stored as an array (just how that function we call works)
    
dictt = [i.to_dict() for i in dictt]
   dictt is just being reused here, it could be any variable name. the part after the assignement is just a for
   loop that iterates though all the enteries we have of the type(location in this example) and calls the to_dict
   function that we made in our models file, for each. this gives us a dictionary of all the enteries that we can
   dump into a json package as, json.dumps takes a dictonary here. 
   
#data = {'Success':json.dumps(dictt)}
    this just makes everything a string, or only returns "success", droped for uselessness as it was not nessary
    
data = json.dumps(dictt)
    again, data is just a variable name, we probley could of reused dictt again, but diden't. json.dumps(dictt)
    takes the dictionary that we made in the previous usefull line, and changes it into a json package.
    
return HttpResponse(data, status = 200)
    views generaly want a HttpResponce return so, it can return html to the front end. here we just return a statis code 
    for "ok" (could be more helpfull, I know) and we also return the data (json dump) of our table.
    
additional notes: back in the models file

'''

''' these are depreciated, from an old database that did not do what we needed it to.
def VLocation(request):
    dictt = models.Location.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VManufacturer(request):
    dictt = models.Manufacturer.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VVendor(request):
    dictt = models.Vendor.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VModelNumber(request):
    dictt = models.ModelNumber.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VService_contract(request):
    dictt = models.Service_contract.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VPort(request):
    dictt = models.Port.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VEquipment(request):
    dictt = models.Equipment.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VUnit(request):
    dictt = models.Unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VComponent(request):
    dictt = models.Component.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VHardDrive(request):
    dictt = models.HardDrive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VMother_board(request):
    dictt = models.Mother_board.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VCentral_processing_unit(request):
    dictt = models.Central_processing_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VOptical_drive(request):
    dictt = models.Optical_drive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VOperating_system(request):
    dictt = models.Operating_system.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VPower_supply_unit(request):
    dictt = models.Power_supply_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VMemory(request):
    dictt = models.Memory.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VRam(request):
    dictt = models.Ram.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VFlash_Memory(request):
    dictt = models.Flash_Memory.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VComputer(request):
    dictt = models.Computer.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VRouter(request):
    dictt = models.Router.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VSwitch(request):
    dictt = models.Switch.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VFirewall(request):
    dictt = models.Firewall.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

this "All" function exist per request the front end devolper, wanted it so it would be easier to make a
"shopping list" like appearance on the front end, which is easier with a dump of EVERYTHING instead of 
makeing repeated calls to all things nessary. it returns all needed in a uber dictionary to assist in making that work

def VAll(request):
    #temp = models.Location.objects.all()
    #dictt = [i.to_dict() for i in temp]
    
    #temp = models.Manufacturer.objects.all()
    #dictt += [i.to_dict() for i in temp]
    
    temp = models.Vendor.objects.all()
    dictt = [i.to_dict() for i in temp]
    
    #temp = models.ModelNumber.objects.all()
    #dictt += [i.to_dict() for i in temp]
    
    temp = models.Service_contract.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Port.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Equipment.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Unit.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Component.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.HardDrive.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Mother_board.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Central_processing_unit.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Optical_drive.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Operating_system.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Power_supply_unit.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Memory.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Ram.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Flash_Memory.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Computer.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Router.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Switch.objects.all()
    dictt += [i.to_dict() for i in temp]
    
    temp = models.Firewall.objects.all()
    dictt += [i.to_dict() for i in temp]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

'''
#----------------------------------------------------Start of actual code-----------------------------------
#line by line explination of the views are at the bottom of the document
def VComputer(request):
    dictt = models.Computer.objects.all()[0]
    HD = dictt.hard_drive_set.all()
    MB = dictt.motherboard_set.all()
    CPU = dictt.central_processing_unit_set.all()
    PSU = dictt.power_supply_unit_set.all()
    OD = dictt.optical_drive_set.all()
    RAM = dictt.ram_set.all()
    OS = dictt.operating_system_set.all()
    FM = dictt.flash_memory_set.all()
    SC = dictt.service_contract_set.all()
    EC = dictt.expansion_card_set.all()
    
    dictt = [i.to_dict() for i in HD]
    dictt += [i.to_dict() for i in MB]
    dictt += [i.to_dict() for i in CPU]
    dictt += [i.to_dict() for i in PSU]
    dictt += [i.to_dict() for i in OD]
    dictt += [i.to_dict() for i in RAM]
    dictt += [i.to_dict() for i in OS]
    dictt += [i.to_dict() for i in FM]
    dictt += [i.to_dict() for i in SC]
    dictt += [i.to_dict() for i in EC]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VHard_drive(request):
    dictt = models.Hard_drive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VMotherboard(request):
    dictt = models.Motherboard.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VCentral_processing_unit(request):
    dictt = models.Central_processing_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VPower_supply_unit(request):
    dictt = models.Power_supply_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VOptical_drive(request):
    dictt = models.Optical_drive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VRAM(request):
    dictt = models.RAM.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VOperating_system(request):
    dictt = models.Operating_system.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VFlash_Memory(request):
    dictt = models.Flash_Memory.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VService_contract(request):
    dictt = models.Service_contract.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VExpansion_card(request):
    dictt = models.Expansion_card.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

'''
    obj = models.Hard_drive.objects.all()[0]
    obj = model_to_dict(obj)
    obj = json.dumps(obj)
    return HttpResponse(obj, status = 200)
'''
'''    
def VFirewall(request):
    dictt = models.Firewall.objects.all()
    dictt = [i.to_dict() for i in dictt]
    #data = {'Success':json.dumps(dictt)}
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)
    
-----calls to change database-----
not yet implemented.
    building = models.CharField(max_length=2)
    room = models.CharField(max_length=4)
'''
'''----------------------this is just a working example of saving to the database on the old database------------
#note, when makeing test, you just make a dictionary of dummy information, then save, then call.
#@csrf_exempt
#@require_http_methods(['POST'])
def Set_Location(request):
    post = request.POST
    package = models.Location()
    package.building = 'ne' #post.building
    package.room = '400' #post.room
    
    package.save()
    data = {'data': 'Request Created'}
    code = 201
    return HttpResponse(simplejson.dumps(package.to_dict()), status=code)
'''

'''------------------------------------Explination of code--------------------------------------------------
-----the following explains what is used for full indivual machine calls
def VComputer(request):
    dictt = models.Computer.objects.all()[0]
dictt is first used here to grab an instance of a computer system from the database. we set it to be from the file
models, the table Computer, then look at all the objects in the table then grab one based on its id

    HD = dictt.hard_drive_set.all()
this line is repeated for all possible objects (with unique variable names) that are parts attached to a machine, here, 
we have HD (short for hard drive) and set it to be an series of instances of all hard drives that are pointing to the 
computer object w pulled. the exact function call/syntax here is [object].[forientable]_set.all(). broken down further, 
object is any single object, that can/does have other tables in the database pointing to it (our computer system). then, 
forientable is a DIFFRENT table that POINTS TO THE FIRST OBJECT, all lower case, underscore set. Django makes this function
by default when you use a forien key in any table for reasons of back referenceing. the end result of this one is it grabs
anything that is pointing to our given computer, that is a hard drive. repeated for all parts that are in any given machine
    
    dictt = [i.to_dict() for i in HD]
this reuses the dictt variable, but could be any name, it takes our HD (hard drive) list of objects made in the previous
command, and itterates (for loop) though it and makes a python dictionary out of it useing the to_dict functions made in the
models file. this is nessary to create the json package that will be sent to the front end.

    dictt += [i.to_dict() for i in MB]
this does the same as the above command, except its using the += operator, as we want to add to that dictionary so we can
send just ONE json package with the information, instead of using a system that requires repeated looped calls from the 
front end.

    data = json.dumps(dictt)
we take the dictionary that is the collection of all instances of objects made from the previous commands and we turn it
into a json package.

    return HttpResponse(data, status = 200)
function return, an instance of object HttpResponce, using the json package we made and a status code (code 200 means OK)
not much logic to return if an error occures, but it what is currently done in this program.
'''
