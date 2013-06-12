from django.contrib.auth.models import User, Group
from rest_framework import serializers
from data.models import Equipment, Computer

class EquipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('description', 'model_num', 'serial_num', 'equip_type', 'location',)

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('description', 'model_num', 'serial_num', 'equip_type', 'location', 'ram', 'max_ram',)

#class Equipment(models.Model):
#	model_num = models.IntegerField()
#	serial_num = models.IntegerField()
#	equip_type = models.ForeignKey(Equip_Type)
#	location = models.ForeignKey(Location)
#	description = models.TextField()