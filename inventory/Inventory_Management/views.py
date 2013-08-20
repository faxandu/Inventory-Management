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

'''
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
'''
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

def VLocation(request):
    dictt = models.Location.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VManufacturer(request):
    dictt = models.Manufacturer.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VVendor(request):
    dictt = models.Vendor.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VModelNumber(request):
    dictt = models.ModelNumber.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VService_contract(request):
    dictt = models.Service_contract.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VPort(request):
    dictt = models.Port.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VEquipment(request):
    dictt = models.Equipment.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VUnit(request):
    dictt = models.Unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VComponent(request):
    dictt = models.Component.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VHardDrive(request):
    dictt = models.HardDrive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VMother_board(request):
    dictt = models.Mother_board.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VCentral_processing_unit(request):
    dictt = models.Central_processing_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VOptical_drive(request):
    dictt = models.Optical_drive.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VOperating_system(request):
    dictt = models.Operating_system.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VPower_supply_unit(request):
    dictt = models.Power_supply_unit.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VMemory(request):
    dictt = models.Memory.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VRam(request):
    dictt = models.Ram.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VFlash_Memory(request):
    dictt = models.Flash_Memory.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VComputer(request):
    dictt = models.Computer.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VRouter(request):
    dictt = models.Router.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VSwitch(request):
    dictt = models.Switch.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)

def VFirewall(request):
    dictt = models.Firewall.objects.all()
    dictt = [i.to_dict() for i in dictt]
    data = {'Success':json.dumps(dictt)}
    data = json.dumps(data)
    return HttpResponse(data, status = 200)
