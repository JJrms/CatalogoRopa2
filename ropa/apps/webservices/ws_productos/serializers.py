from rest_framework import serializers
from ropa.apps.ventas.models import Ropa, Marca, Categoria,Color


class ropa_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ropa
		fields = ('url', 'descripcion', 'status', 'nombre', 'imagen', 'precio')

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url',  'nombre',)
	
class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('url','nombre',)

class color_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Color
		fields = ('url','nombre',)
#https://pypi.python.org/pypi/djangorestframework/2.3.14