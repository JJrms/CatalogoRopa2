# Create your views here.
from django.http import HttpResponse
from ropa.apps.ventas.models import *
from django.core import serializers
from .serializers import *
from rest_framework import viewsets

def ws_productos_view(request):
	data = serializers.serialize("json", Ropa.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')



class ropa_viewset(viewsets.ModelViewSet):
	queryset = Ropa.objects.all()
	serializer_class = ropa_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer

class color_viewset(viewsets.ModelViewSet):
	queryset = Color.objects.all()
	serializer_class = color_serializer

		
		