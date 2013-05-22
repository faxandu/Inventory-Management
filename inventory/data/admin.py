from django.contrib import admin
from data.models import Equipment, Equip_Type, Location

#class EquipAdmin(admin.ModelAdmin):
#    fields = ['model_num', 'serial_num']

admin.site.register(Equipment)
