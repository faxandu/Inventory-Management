#from django.contrib.auth.models import User, Group #this is typicaly default, wasented needed
from django.http import HttpResponse #this is what is returned to the front end for sending data
from Inventory_Management import models #this is the models file that defines our database
#from django.core import serializers #was used once, now unused
import json # contains the dumps function, which turns python dictionary to a readable json package
import time # used in one function to in case its needed to auto-fill in time
#for auth
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.http import require_http_methods #unused but left in case
from django.forms.models import model_to_dict #unused, but comes as a default, used custom functions

from django.utils import simplejson

#----------------------------------------------------Start of code to read database-----------------------------------
#line by line explination of the views are at first instance of them, as many are like. explinations
#are set up as if you know nothing about python so may seems abit....condacending

'''
def VModelnum(request):
--define a function with the name vModelnum, taking a parameter called request
--request holds POST which is what was passed into our system via POST request

    temp = models.Modelnum.objects.get(model_type=request.POST.model_type)
    -- make a temp variable, and take an instance of modelnum from out of models, and call the
    -- object objects.get (this is a query that just digs out all the enteries in the table 
    -- modeltype WHERE the type is what was passed in)
    dictt = [i.to_dict() for i in temp]
    -- this is a quick for loop, take all the instances pulled from that query, (in temp) and call
    -- the function to.dict (defined on the model file, details there) on all instances of 
    -- the class (again, details in models) to make a dictionary list which can be..
    data = json.dumps(dictt)
    -- turned into a json package with the json.dumps function which we then..
    return HttpResponse(data, status = 200)
    -- return to the front end, with a status code confirming "ok" (yes, thats what it stands for)
'''
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

#-------------------------------------machine sets-------------------------------------------------------
'''
@csrf_exempt
-- this is called a decerator, all i know is that we need this one to modify the database
-- its like a function that modifies the function (i think)
def Set_Computer(request):
-- make a function called Set_computer, taking in an variable called request
    package = models.Computer()
    -- take our model Computer, and make a blank instance of it
    if request.POST['acquisition_date'] == "":
    -- if the POST data has blank data...
        package.acquisition_date = time.strftime('%Y-%m-%d')
        -- set it to be the current time in a format that SQL will accept
    else:
        package.acquisition_date = request.POST['acquisition_date']
        -- else, set the POST data passed in as the field

    package.IS = request.POST['IS']
    -- this like most of what follows, simply set what is passed into to our once blank entery
    package.serial = request.POST['serial']
    package.model = request.POST['model']
    if request.POST['in_use'] == "false":
        package.in_use = False
    else:
        package.in_use = True
    -- this if else was nessary as the POST brings in a string, but the data base actualy
    -- stores a boolean. so a little bit of logic was nessary
            
    package.location = request.POST['location']
    try:
        package.save()
    -- try to save the model we just crafted to the database, if it throws an error...
    except:
        return HttpResponse("there was an error in the package", status=400)
    -- return a string informing the front end there was an error with a generic error code 400
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)
    -- when done, return what we made to the front end for validation (if they choose too) and
    -- and error code specifying that the record was created

'''

@csrf_exempt
def Set_Computer(request):
    package = models.Computer()
    if request.POST['acquisition_date'] == "":
        package.acquisition_date = time.strftime('%Y-%m-%d')
    else:
        package.acquisition_date = request.POST['acquisition_date']

    package.IS = request.POST['IS']
    package.serial = request.POST['serial']
    package.model = request.POST['model']
    if request.POST['in_use'] == "false":
        package.in_use = False
    else:
        package.in_use = True
            
    package.location = request.POST['location']
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Router(request):
    package = models.Router()
    if request.POST['acquisition_date'] == "":
        package.acquisition_date = time.strftime('%Y-%m-%d')
    else:
        package.acquisition_date = request.POST['acquisition_date']

    package.IS = request.POST['IS']
    package.serial = request.POST['serial']
    package.model = request.POST['model']
    if request.POST['in_use'] == "false":
        package.in_use = False
    else:
        package.in_use = True
            
    package.location = request.POST['location']
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Switch(request):
    package = models.Switch()
    if request.POST['acquisition_date'] == "":
        package.acquisition_date = time.strftime('%Y-%m-%d')
    else:
        package.acquisition_date = request.POST['acquisition_date']

    package.IS = request.POST['IS']
    package.serial = request.POST['serial']
    package.model = request.POST['model']
    if request.POST['in_use'] == "false":
        package.in_use = False
    else:
        package.in_use = True
            
    package.location = request.POST['location']
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Firewall(request):
    package = models.Firewall()
    if request.POST['acquisition_date'] == "":
        package.acquisition_date = time.strftime('%Y-%m-%d')
    else:
        package.acquisition_date = request.POST['acquisition_date']

    package.IS = request.POST['IS']
    package.serial = request.POST['serial']
    package.model = request.POST['model']
    if request.POST['in_use'] == "false":
        package.in_use = False
    else:
        package.in_use = True
            
    package.location = request.POST['location']
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_Server(request):
    package = models.Server()
    if request.POST['acquisition_date'] == "":
        package.acquisition_date = time.strftime('%Y-%m-%d')
    else:
        package.acquisition_date = request.POST['acquisition_date']

    package.IS = request.POST['IS']
    package.serial = request.POST['serial']
    package.model = request.POST['model']
    if request.POST['in_use'] == "false":
        package.in_use = False
    else:
        package.in_use = True
            
    package.location = request.POST['location']
    try:
        package.save()
    except:
        return HttpResponse("there was an error in the package", status=400)
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

#-------------------------------------------part sets-------------------------------------------------------
# this function just makes a new model in the data base, it is called when something is added
# to the database that dosen't exist, it adds it. was a requested feature
def Set_model(num, model_type):
    temp=models.Modelnum()
    temp.model_number = num
    temp.model_type = model_type
    temp.save()

'''
@csrf_exempt
-- this is called a decerator, all i know is that we need this one to modify the database
-- its like a function that modifies the function (i think)
def Set_Hard_drive(request):
-- define a function called Set_Hard_drive, taking a variable called request which holds the POST data
    package = models.Hard_drive()
    -- make a blank instance of the hard drive model
    package.total_GB = request.POST['total_GB']
    -- this is the same for many of the following, but take our package, and set its field to be
    -- what is in the passed in post data
    temp = models.Modelnum.objects.all()
    -- take a temp variable, and make it equal to every instance we have of models
    if temp.filter(model_number=request.POST['model']).exists():
    -- if what was passed in to our post exist inside the temp which holds all models...
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        -- then set in our package model to the instance in the modelnum table
    else:
        Set_model(request.POST['model'], "HD")
        -- otherwise make it...
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        -- and then set the newly made instance to our package
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])

    if package.model.model_type != 'HD':
        return HttpResponse('Error, model type is not for a Hard Drive', status = 406)
        -- if the model in the database is NOT what we are trying to set, inform user and
        -- return an error. if a model was made, it was made for what called it, so no
        -- confilct if one was made
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)
    -- save the package and return whas was added and a record created status code
'''

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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
    if package.model.model_type != 'OD':
        return HttpResponse('Error, model type is not for an Optical Drive', status = 406)
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

@csrf_exempt
def Set_RAM(request):
    package = models.RAM()
    package.size_in_gigs = request.POST['size_in_gigs']
    temp = models.Modelnum.objects.all()
    
    if temp.filter(model_number=request.POST['model']).exists():
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
    else:
        Set_model(request.POST['model'], "RM")
        package.model = models.Modelnum.objects.get(model_number=request.POST['model'])
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
        
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
def Set_Additional_features(request):
    package = models.Expansion_card()
    package.description = request.POST.description
        
    package.location = models.Equipment.objects.get(serial=request.POST['location'])
    
    package.save()
    return HttpResponse(simplejson.dumps(package.to_dict()), status=201)

#---------------------------------------Deleting machines--------------------------------

def Del_Equipment(request):
    temp = models.Equipment.objects.all()
    if temp.filter(serial=request.POST['serial']).exists():
        killme = models.Equipment.objects.filter(serial=request.POST['serial'])
        killme.delete()
        return HttpResponse("Entry Deleted", status=200)
    else:
        return HttpResponse("error locating record", status=304)
        
