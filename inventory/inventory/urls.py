from django.conf.urls import patterns, include, url
from rest_framework import routers
from Inventory_Management import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#router = routers.DefaultRouter()
#router.register(r'Equip', views.UserViewSet)
#router.register(r'Computer', views.ComputerViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^inventory/', include('inventory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Inventory_Management/', include('Inventory_Management.urls')),
    #url(r'^Equip/$', views.UserViewSet.as_view()),
    #url(r'^Computer/$', views.ComputerViewSet.as_view()),
)
#url(r'^events/$', views.EventList.as_view()),