from django.contrib import admin
from Inventory_Management.models import *

#just a register dump so we can modify anything inside the admin interface
admin.site.register(Equipment)
admin.site.register(Unit)
admin.site.register(Component)
admin.site.register(Location)
admin.site.register(Manufacturer)
admin.site.register(Vendor)
admin.site.register(ModelNumber)
admin.site.register(Memory)
admin.site.register(Ram)
admin.site.register(Flash_Memory)
admin.site.register(HardDrive)
admin.site.register(Mother_board)
admin.site.register(Central_processing_unit)
admin.site.register(Optical_drive)
admin.site.register(Operating_system)
admin.site.register(Power_supply_unit)
admin.site.register(Service)
admin.site.register(Router)
admin.site.register(Computer)