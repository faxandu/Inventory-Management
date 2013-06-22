from django.conf.urls import patterns, url, include
from rest_framework import routers
from Inventory_Management import views

router = routers.DefaultRouter()
router.register(r'Equip', views.UserViewSet)
router.register(r'Computer', views.ComputerViewSet)

urlpatterns = patterns('',
	url(r'^', include(router.urls)),
#    url(r'^$', views.index, name='index'),
    url(r'^Equip/$', views.UserViewSet.as_view()),
    url(r'^Computer/$', views.ComputerViewSet.as_view()),
    url('^(?P<value>.+)/$', views.Custom.as_view()),
)