from django.contrib import admin
from Inventory_Management.models import *

#the [name]Admin is to make readin the admin pannel plausable, it adds in the lines that specify its name, tag, and if
#its in use for main towers, for componets it makes the serials the visible part of them
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'in_use', 'IS')
    fields = ['machine_name',]

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'in_use', 'IS')

class RouterAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'in_use', 'IS')

class SwitchAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'in_use', 'IS')

class FirewallAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'in_use', 'IS')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'in_use', 'IS')

#just a register dump so we can modify anything inside the admin interface
admin.site.register(Equipment, EquipmentAdmin)
#admin.site.register(Manufacturer)
admin.site.register(Serial)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Router, RouterAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Firewall, FirewallAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(Hard_drive)
admin.site.register(Motherboard)
admin.site.register(Central_processing_unit)
admin.site.register(Power_supply_unit)
admin.site.register(Optical_drive)
admin.site.register(RAM)
admin.site.register(Operating_system)
admin.site.register(Flash_Memory)
admin.site.register(Service_contract)
admin.site.register(Expansion_card)
