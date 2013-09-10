from django.conf.urls import patterns, url, include
#from rest_framework import routers


from Inventory_Management import views

'''
router = routers.DefaultRouter()

#base 5
router.register(r'all/Location', views.VLocation)
router.register(r'all/Manufacturer', views.VManufacturer)
router.register(r'all/ModelNumber', views.VModelNumber)
router.register(r'all/Service', views.VService_contract)
router.register(r'all/Port', views.VPort)
#main all
router.register(r'all/Equipment', views.VEquipment)
#main 2
router.register(r'all/Unit', views.VUnit)
router.register(r'all/Component', views.VComponent)
#componet 7
router.register(r'all/HardDrive', views.VHardDrive)
router.register(r'all/Mother_board', views.VMother_board)
router.register(r'all/Central_processing_unit', views.VCentral_processing_unit)
router.register(r'all/Optical_drive', views.VOptical_drive)
router.register(r'all/Operating_system', views.VOperating_system)
router.register(r'all/Power_supply_unit', views.VPower_supply_unit)
router.register(r'all/Memory', views.VMemory)
#these are derived from memory
router.register(r'all/Ram', views.VRam)
router.register(r'all/Flash_Memory', views.VFlash_Memory)
#unit 2
router.register(r'all/Router', views.VRouter)
router.register(r'all/Computer', views.VComputer)
#from router
router.register(r'all/Switch', views.VSwitch)
router.register(r'all/Firewall', views.VFirewall)

urlpatterns = router.urls

'''

#the following maintained for reasons of reference/potential expantion
#urlpatterns += patterns('',
#	url(r'^Manufacturer/(?P<Mname>.+)/$', views.VManufacturer.as_view()),
#	)Service_contract

urlpatterns = patterns('',
	url(r'^all/Location', views.VLocation),
	url(r'^all/Manufacturer', views.VManufacturer),
	url(r'^all/Vendor', views.VVendor),
	url(r'^all/ModelNumber', views.VModelNumber),
	url(r'^all/Service_contract', views.VService_contract),
	url(r'^all/Port', views.VPort),
	url(r'^all/Equipment', views.VEquipment),
	url(r'^all/Unit', views.VUnit),
	url(r'^all/Component', views.VComponent),
	url(r'^all/HardDrive', views.VHardDrive),
	url(r'^all/Mother_board', views.VMother_board),
	url(r'^all/Central_processing_unit', views.VCentral_processing_unit),
	url(r'^all/Optical_drive', views.VOptical_drive),
	url(r'^all/Operating_system', views.VOperating_system),
	url(r'^all/Power_supply_unit', views.VPower_supply_unit),
	url(r'^all/Memory', views.VMemory),
	url(r'^all/Ram', views.VRam),
	url(r'^all/Flash_Memory', views.VFlash_Memory),
	url(r'^all/Computer', views.VComputer),
	url(r'^all/Router', views.VRouter),
	url(r'^all/Switch', views.VSwitch),
	url(r'^all/Firewall', views.VFirewall),
	url(r'^all/All', views.VAll),
	)
