# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from data.serializers import EquipSerializer
from data.models import Equipment

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipSerializer