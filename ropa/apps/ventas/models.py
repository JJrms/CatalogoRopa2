from django.db import models
from django.conf.urls.defaults import url

# Create your models here.

class Marca(models.Model):
	nombre_marca =  models.CharField(max_length = 100)
	
	def __unicode__(self):
		return self.nombre_marca

class Color (models.Model):
	nombre_color	= models.CharField(max_length = 200)

	def  __unicode__(self):
		return self.nombre_color

class Categoria(models.Model):
	nombre= models.CharField(max_length = 100)
	descripcion= models.CharField(max_length = 500)

	def __unicode__(self):
		return self.nombre
		
class Ropa(models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Ropa/%s/%s"%(self.nombre,str(filename))
		return ruta
	marca 		= models.ForeignKey(Marca)
	color 		= models.ManyToManyField(Color)
	Categoria	= models.ManyToManyField(Categoria)	
	nombre 		= models.CharField(max_length = 100)
	descripcion	= models.CharField(max_length = 500)
	status		= models.BooleanField(default = True)
	imagen		= models.ImageField(upload_to = url, null = True, blank =True)
	precio		= models.DecimalField(max_digits = 10, decimal_places = 2)
	stock		= models.IntegerField()

	def __unicode__ (self):
		return self.marca.nombre_marca