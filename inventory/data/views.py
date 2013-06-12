# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from data.serializers import EquipSerializer, ComputerSerializeras
from data.models import Equipment, Computer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipSerializer

class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer