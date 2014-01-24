from django.conf.urls import patterns, url, include
#from rest_framework import routers


from Inventory_Management import views

urlpatterns = patterns('',
       url(r'^all/Modelnum', views.VModelnum),
       url(r'^all/Equipment', views.VEquipment),
       url(r'^all/Computer', views.VComputer),
       url(r'^all/Router', views.VRouter),
       url(r'^all/Switch', views.VSwitch),
       url(r'^all/Firewall', views.VFirewall),
       url(r'^all/Server', views.VServer),
       
       url(r'^all/Hard_drive', views.VHard_drive),
       url(r'^all/Motherboard', views.VMotherboard),
       url(r'^all/Central_processing_unit', views.VCentral_processing_unit),
       url(r'^all/Power_supply_unit', views.VPower_supply_unit),
       url(r'^all/Optical_drive', views.VOptical_drive),
       url(r'^all/RAM', views.VRAM),
       url(r'^all/Operating_system', views.VOperating_system),
       url(r'^all/Flash_memory', views.VFlash_memory),
       url(r'^all/Service_contract', views.VService_contract),
       url(r'^all/Expansion_card', views.VExpansion_card),
       
       url(r'^set/Computer', views.Set_Computer),
       url(r'^set/Router', views.Set_Router),
       url(r'^set/Switch', views.Set_Switch),
       url(r'^set/Firewall', views.Set_Firewall),
       url(r'^set/Server', views.Set_Server),
       
       url(r'^set/Hard_drive', views.Set_Hard_drive),
       url(r'^set/Motherboard', views.Set_Motherboard),
       url(r'^set/Central_processing_unit', views.Set_Central_processing_unit),
       url(r'^set/Power_supply_unit', views.Set_Power_supply_unit),
       url(r'^set/Optical_drive', views.Set_Optical_drive),
       url(r'^set/RAM', views.Set_RAM),
       url(r'^set/Operating_system', views.Set_Operating_system),
       url(r'^set/Flash_memory', views.Set_Flash_memory),
       url(r'^set/Service_contract', views.Set_Service_contract),
       url(r'^set/Expansion_card', views.Set_Expansion_card),
       url(r'^del/machine', views.Del_Equipment),
)
