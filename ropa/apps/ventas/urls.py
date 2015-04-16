from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ropa.apps.ventas.views',
		url(r'^add/ropa/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/ropa/(?P<id_prod>.*)/$','edit_producto_view', name = 'vista_editar_producto'),
	)

