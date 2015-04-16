from django.conf.urls.defaults import patterns, url
from django.conf.urls import include
from rest_framework import routers
from ropa.apps.webservices.ws_productos.views import  *
router = routers.DefaultRouter()
router.register(r'ropa', ropa_viewset)
router.register(r'marca', marca_viewset)
router.register(r'categoria', categoria_viewset)

urlpatterns = patterns('ropa.apps.webservices.ws_productos.views',		
		url(r'^ws/productos/$','ws_productos_view',name = 'ws_productos_url'),
		url(r'^api/', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	)