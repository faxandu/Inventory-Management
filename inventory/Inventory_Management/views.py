#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets, generics#generics is here for if we need generics.ListAPIView
#from Inventory_Management import serializers
from django.http import HttpResponse
from Inventory_Management import models
from django.core import serializers
import json
import time
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
    dictt = models.Flash_memory.objects.all()
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
@csrf_exempt
def Set_Computer(request):
    package = models.Computer()
#    try:
#        package.acquisition_date = request.POST['acquisition_date']
#    except:
    package.acquisition_date = time.strftime('%Y-%m-%d')
    try:
        package.IS = request.POST['IS']
    except:
        package.IS = ""
    try:
        package.machine_name = request.POST['machine_name']
    except:
        return HttpResponse("unique machine_name Required", status=400)
    try:
        package.in_use = request.POST['in_use']
    except:
        package.in_use = True
    try:
        package.location = request.POST['location']
    except:
        package.location = ""
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Router(request):
    package = models.Router()
    try:
        package.acquisition_date = request.POST['acquisition_date']
    except:
        package.acquisition_date = time.strftime('%Y-%m-%d')
    try:
        package.IS = request.POST['IS']
    except:
        package.IS = ""
    try:
        package.machine_name = request.POST['machine_name']
    except:
        return HttpResponse("unique machine_name Required", status=400)
    try:
        package.in_use = request.POST['in_use']
    except:
        package.in_use = True
    try:
        package.location = request.POST['location']
    except:
        package.location = ""
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Switch(request):
    package = models.Switch()
    try:
        package.acquisition_date = request.POST['acquisition_date']
    except:
        package.acquisition_date = time.strftime('%Y-%m-%d')
    try:
        package.IS = request.POST['IS']
    except:
        package.IS = ""
    try:
        package.machine_name = request.POST['machine_name']
    except:
        return HttpResponse("unique machine_name Required", status=400)
    try:
        package.in_use = request.POST['in_use']
    except:
        package.in_use = True
    try:
        package.location = request.POST['location']
    except:
        package.location = ""
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Firewall(request):
    package = models.Firewall()
    try:
        package.acquisition_date = request.POST['acquisition_date']
    except:
        package.acquisition_date = time.strftime('%Y-%m-%d')
    try:
        package.IS = request.POST['IS']
    except:
        package.IS = ""
    try:
        package.machine_name = request.POST['machine_name']
    except:
        return HttpResponse("unique machine_name Required", status=400)
    try:
        package.in_use = request.POST['in_use']
    except:
        package.in_use = True
    try:
        package.location = request.POST['location']
    except:
        package.location = ""
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Server(request):
    package = models.Server()
    try:
        package.acquisition_date = request.POST['acquisition_date']
    except:
        package.acquisition_date = time.strftime('%Y-%m-%d')
    try:
        package.IS = request.POST['IS']
    except:
        package.IS = ""
    try:
        package.machine_name = request.POST['machine_name']
    except:
        return HttpResponse("unique machine_name Required", status=400)
    try:
        package.in_use = request.POST['in_use']
    except:
        package.in_use = True
    try:
        package.location = request.POST['location']
    except:
        package.location = ""
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

#-------------------------------------------part sets-------------------------------------------------------
def Set_model(num, model_type):
    temp=models.Modelnum()
    temp.model_number = num
    temp.model_type = model_type
    temp.save()

@csrf_exempt
def Set_Hard_drive(request):
    package = models.Hard_drive()
    package.total_GB = request.POST['total_GB']
    temp = models.Modelnum.objects.all()
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "HD")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'HD':
        return HttpResponse('Error, model type is not for a Hard Drive', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)
    
@csrf_exempt
def Set_Motherboard(request):
    package = models.Motherboard()
    temp = models.Modelnum.objects.all()
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "MB")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'MB':
        return HttpResponse('Error, model type is not for Motherboards', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Central_processing_unit(request):
    package = models.Central_processing_unit()
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "CP")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'CP':
        return HttpResponse('Error, model type is not for a CPU', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Power_supply_unit(request):
    package = models.Power_supply_unit()
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "PS")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'PS':
        return HttpResponse('Error, model type is not for a Power Supply', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Optical_drive(request):
    package = models.Optical_drive()
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "OD")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'OD':
        return HttpResponse('Error, model type is not for an Optical Drive', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_RAM(request):
    package = models.RAM()
    package.size_in_gigs = request.POST.size_in_gigs
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "RM")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'RM':
        return HttpResponse('Error, model type is not for RAM', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Operating_system(request):
    package = models.Operating_system()
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "OS")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'OS':
        return HttpResponse('Invalid Operating System', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Flash_memory(request):
    package = models.Flash_memory()
    package.size_in_megs = request.POST.size_in_megs
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "FM")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
        
    if package.model.model_type != 'FM':
        return HttpResponse('Error, model type is not for Flash Memory', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Service_contract(request):
    package = models.Service_contract()
    package.expire_date = post.expire_date
    package.additional_notes = post.additional_notes
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Expansion_card(request):
    package = models.Expansion_card()
    package.description = request.POST.description
        
    package.location = models.Equipment.objects.get(machine_name=request.POST['location'])
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

#---------------------------------------Deleting machines--------------------------------

def Del_Equipment(request):
    temp = models.Equipment.objects.all()
    if temp.filter(machine_name=request.POST['machine_name']).exists():
        killme = models.Equipment.objects.filter(machine_name=request.POST['machine_name'])
        killme.delete()
        return HttpResponse("Entry Deleted", status=200)
    else:
        return HttpResponse("error locating record", status=304)
        
'''------------------------------------Explination of code--------------------------------------------------
-----calls to view database

def VComputer(request):
--define function called VCompter, take in an instance of a HTML request
    temp = models.Computer.objects.all()
--make a temp variable as querry of the computer object, and have it return all instances of it
    dictt = [i.to_dict() for i in temp]
--if you look into the models file, there is a to_dict function for all tables(classes) this function
--takes a SINGLE instance of the class and turns it into a python dictionary, which is needed for 
--convertion to json pack which is what is sent to the front end.
    data = json.dumps(dictt)
--we take that dictionary we made, and turn it into a json package. this is a default function from import json.
    return HttpResponse(data, status = 200)
--return an instance of HttpResponce, which djano uses, with the json package and a status code

-----calls to add machines

@csrf_exempt
--this is a decorator that is required
def Set_Computer(request):
    package = models.Computer()
--make a new instance of computer
--the following try excepts are just a way of testing if a variable exist, as if it dosen't it will error
--we simply catch it and then do an assignment to a blank/relevent value for the field. if it does exist,
--we then let the inital direct assignment go on though.
    try:
        package.acquisition_date = request.POST['date']
    except:
        package.acquisition_date = time.strftime('%Y-%m-%d')
--the time.setftime is a formatted time string, that should be accepted by the database, its the current date
    try:
        package.IS = request.POST['IS']
    except:
        package.IS = ""
    try:
        package.machine_name = request.POST['machine_name']
    except:
        package.machine_name = ""
    try:
        package.in_use = request.POST['in_use']
    except:
        package.in_use = True
    try:
        package.location = request.POST['location']
    except:
        package.location = ""
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
--if there's a problem saving, the we return an error.
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

-----calls to add parts

def Set_Hard_drive(request):
    post = request.POST
--same as above, for convience
    package = models.Hard_drive()
--same as above, sets a blank instance of the part
    package.total_GB = post.total_GB
--"basic" fields are just given
    temp = models.Modelnum.objects.all()
--for ease of front end use, we take an instance of all models in the database
    if temp.filter(model_number=post.model_number).exist():
        package.model = models.Modelnum.objects.get(model_number=post.model_number)
--we check if that model exist in our database
    else:
        Set_model(post.model, "HD")
--if it does not, we make one
    if isinstance(post.location, int):
        package.location = models.Equipment.objects.get(id=post.location)
--if it's an intiger, then treat it like a primary key
    elif isinstance(post.location, str):
        package.location = models.Equipment.objects.get(machine_name=post.location)
--if its a string, treat it like a model number
    else:
        return HttpResponse('Error, Location Invalid', status = 406)
--if its not either, return an error

    if package.model.model_type != 'HD':
        return HttpResponse('Error, model type is not for a Hard Drive', status = 406)
--check if its the right type of model, so we don't get drives labled as motherbored.
    package.save()
--save it to the database.
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)
'''
