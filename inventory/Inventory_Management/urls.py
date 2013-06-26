from django.conf.urls import patterns, url, include
from rest_framework import routers
from Inventory_Management import views

router = routers.DefaultRouter()

#base 4
router.register(r'all/Location', views.VLocation)
router.register(r'all/Manufacturer', views.VManufacturer)
router.register(r'all/ModelNumber', views.VModelNumber)
router.register(r'all/Service', views.VService)
#main all
router.register(r'all/Equipment', views.VEquipment)
#main 2
router.register(r'all/Unit', views.VUnit)
router.register(r'all/Component', views.VComponent)
#componet 7
router.register(r'all/Memory', views.VMemory)
router.register(r'all/HardDrive', views.VHardDrive)
router.register(r'all/Mother_board', views.VMother_board)
router.register(r'all/Central_processing_unit', views.VCentral_processing_unit)
router.register(r'all/Optical_drive', views.VOptical_drive)
router.register(r'all/Operating_system', views.VOperating_system)
router.register(r'all/Power_supply_unit', views.VPower_supply_unit)
#unit 2
router.register(r'all/Router', views.VRouter)
router.register(r'all/Computer', views.VComputer)

urlpatterns = router.urls

#the following maintained for reasons of reference/potential expantion
#urlpatterns += patterns('',
#	url(r'^Manufacturer/(?P<Mname>.+)/$', views.VManufacturer.as_view()),
#	)