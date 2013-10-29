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
#----------------------------------------------------Start of code to read database-----------------------------------
#line by line explination of the views are at the bottom of the document

def VModelnum(request):
    temp = models.Modelnum.objects.get(model_type=request.POST.model_type)
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VEquipment(request): #models.Computer.objects.count()
    temp = models.Equipment.objects.all()
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VComputer(request):
    temp = models.Computer.objects.all()
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VRouter(request):
    temp = models.Router.objects.all()
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VSwitch(request):
    temp = models.Switch.objects.all()
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VFirewall(request):
    temp = models.Firewall.objects.all()
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VServer(request):
    temp = models.Server.objects.all()
    dictt = [i.to_dict() for i in temp]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)
    
def VHard_drive(request):
    dictt = models.Hard_drive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VMotherboard(request):
    dictt = models.Motherboard.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VCentral_processing_unit(request):
    dictt = models.Central_processing_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VPower_supply_unit(request):
    dictt = models.Power_supply_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VOptical_drive(request):
    dictt = models.Optical_drive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VRAM(request):
    dictt = models.RAM.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VOperating_system(request):
    dictt = models.Operating_system.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VFlash_memory(request):
    dictt = models.Flash_Memory.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VService_contract(request):
    dictt = models.Service_contract.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)

def VExpansion_card(request):
    dictt = models.Expansion_card.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = json.dumps(dictt)
    return HttpResponse(data, status = 200)
#--------------------------------------Start of code for modifying database---------------------------------
'''
class Equipment(models.Model):
    acquisition_date = models.DateField(blank = True, null = True)
    #service_tag = models.CharField(max_length = 35, blank = True, null = True)
    IS = models.CharField(max_length = 35, blank = True, unique = False, null = True)
    machine_name = models.CharField(max_length = 100, unique = False, blank = True, null = True)
    in_use = models.BooleanField()
    location = models.TextField(blank = True, null = True)
'''
#-------------------------------------machine sets-------------------------------------------------------
def Set_Computer(request):
    post = request.POST
    package = models.Computer()
    package.acquisition_date = post.acquisition_date
    package.IS = post.IS
    package.machine_name = post.machine_name
    package.in_use = post.in_use
    package.location = post.location
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Router(request):
    post = request.POST
    package = models.Router()
    package.acquisition_date = post.acquisition_date
    package.IS = post.IS
    package.machine_name = post.machine_name
    package.in_use = post.in_use
    package.location = post.location
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Switch(request):
    post = request.POST
    package = models.Switch()
    package.acquisition_date = post.acquisition_date
    package.IS = post.IS
    package.machine_name = post.machine_name
    package.in_use = post.in_use
    package.location = post.location
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Firewall(request):
    post = request.POST
    package = models.Firewall()
    package.acquisition_date = post.acquisition_date
    package.IS = post.IS
    package.machine_name = post.machine_name
    package.in_use = post.in_use
    package.location = post.location
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Server(request):
    post = request.POST
    package = models.Server()
    package.acquisition_date = post.acquisition_date
    package.IS = post.IS
    package.machine_name = post.machine_name
    package.in_use = post.in_use
    package.location = post.location
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

#-------------------------------------------part sets-------------------------------------------------------

def Set_Hard_drive(request):
    post = request.POST
    package = models.Hard_drive()
    package.total_GB = post.total_GB
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'HD':
        return HttpResponse('Error, model type is not for a Hard Drive', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Motherboard(request):
    post = request.POST
    package = models.Motherboard()
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'MB':
        return HttpResponse('Error, model type is not for Motherboards', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Central_processing_unit(request):
    post = request.POST
    package = models.Central_processing_unit()
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'CP':
        return HttpResponse('Error, model type is not for a CPU', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)


def Set_Power_supply_unit(request):
    post = request.POST
    package = models.Power_supply_unit()
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'PS':
        return HttpResponse('Error, model type is not for a Power Supply', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Optical_drive(request):
    post = request.POST
    package = models.Optical_drive()
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'OD':
        return HttpResponse('Error, model type is not for an Optical Drive', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_RAM(request):
    post = request.POST
    package = models.RAM()
    package.size_in_gigs = post.size_in_gigs
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'RM':
        return HttpResponse('Error, model type is not for RAM', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Operating_system(request):
    post = request.POST
    package = models.Operating_system()
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'OS':
        return HttpResponse('Error, model type is not for Operating Systems', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Flash_memory(request):
    post = request.POST
    package = models.Flash_memory()
    package.size_in_megs = post.size_in_megs
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'FM':
        return HttpResponse('Error, model type is not for Flash Memory', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Service_contract(request):
    post = request.POST
    package = models.Service_contract()
    package.expire_date = post.expire_date
    package.additional_notes = post.additional_notes
    package.model = models.Modelnum.objects.get(model_number=post.model)
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
        
    if package.model.model_type != 'RM':
        return HttpResponse('Error, model type is not for RAM', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

def Set_Expansion_card(request):
    post = request.POST
    package = models.Expansion_card()
    package.description = post.description
    
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)


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
