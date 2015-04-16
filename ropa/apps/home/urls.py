from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ropa.apps.home.views',
		url(r'^$','paginaprincipal_view', name = 'vista_principal'),    
		url(r'^about/$', 'about_view', name = 'vista_about'),
		url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		url(r'^ropas/page/(?P<pagina>.*)/$','ropas_view', name = 'vista_ropas '),
		url(r'^ropa/(?P<id_ropa>.*)/$', 'single_ropa_view', name = 'vista_ropa'),
	)