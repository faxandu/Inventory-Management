from django.conf.urls import patterns, url, include
from rest_framework import routers
from Inventory_Management import views

router = routers.DefaultRouter()
#router.register(r'showall/Manufacturer', views.VManufacturer)
router.register(r'showall/Vendor', views.VVendor)
router.register(r'showall/Location', views.VLocation)
router.register(r'showall/ModelNumber', views.VModelNumber)
#router.register(r'Computer', views.ComputerViewSet)
#router.register(r'^accounts/{pk}/$', views.Custom)
#this line creates the urlpatterens based on the registered routes
urlpatterns = router.urls

urlpatterns += patterns('',
	url(r'^showall/Manufacturer/(?P<username>.+)/$', views.VManufacturer))
#	url(r'^', include(router.urls)),
##    url(r'^$', views.index, name='index'),
#    url(r'^Equip/$', views.UserViewSet.as_view()),
#    url(r'^Computer/$', views.ComputerViewSet.as_view()),
#    url(r'^(?P<value>\w+)/$', views.Custom.as_view()),
#)