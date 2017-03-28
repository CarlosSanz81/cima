from __future__ import unicode_literals
from django.db import models
from clientes.models import Clientes
from papeles.models import Papel
from acabado.models import Acabado
from modo.models import Modo
from gramajes.models import Gramaje
from codpostales.models import CodigosPostales
from transporte.models import Transporte
from iva.models import Iva
from comercial.models import Comercial
from laminado.models import TipoLaminado




# Create your models here.

class Parte(models.Model):
	parte = models.IntegerField(unique=True)
	cliente = models.ForeignKey(Clientes)

	class hallarcliente(models.Model):
		user = models.ForeignKey(Clientes)
		
		def __str__(self):
			return '%s ' == cliente % (self.user.numeroCliente)

	numeroCliente = hallarcliente()
	titulo = models.CharField(max_length=50)
	isbn = models.DecimalField(max_digits=13, decimal_places=0, blank=True)
	acabado = models.ForeignKey(Acabado)
	ancho = models.DecimalField(max_digits=6, decimal_places=3)
	largo = models.DecimalField(max_digits=6, decimal_places=3)
	modo = models.ForeignKey(Modo)
	cantidad = models.IntegerField(default=0)
	paginas = models.IntegerField(default=0)
	carasInterior = models.BooleanField(default=True)
	papelInteriorUno = models.ForeignKey(Papel, related_name= '+')
	papelInteriorDos = models.ForeignKey(Papel, related_name= '+')
	gramajeInteriorUno = models.ManyToManyField(Gramaje, related_name= '+')
	gramajeInteriorDos = models.ManyToManyField(Gramaje, related_name= '+')
	papelPortada = models.OneToOneField(Papel, related_name= '+')
	gramajePortada = models.ForeignKey(Gramaje, related_name= '+')
	carasPortada =  models.BooleanField(default=False)
	laminado = models.BooleanField(default=False)
	tipoLaminado = models.ForeignKey(TipoLaminado, blank=True)
	solapas = models.BooleanField(default=False)
	mmSolapas = models.DecimalField(max_digits=3, decimal_places=0, blank=True)
	retractilado = models.BooleanField(default=False)
	codpostal = models.ForeignKey(CodigosPostales)
	transp = models.ForeignKey(Transporte)
	comentarios = models.CharField(max_length=255)
	venta = models.DecimalField(max_digits=10, decimal_places=4)
	fechaEntrada = models.DateTimeField(auto_now_add=True)
	fechaModificacion = models.DateTimeField(auto_now=True)
	fechaEntrega = models.DateField(blank=False, null=True)
	iva = models.ForeignKey(Iva)
	comercial = models.ForeignKey(Comercial)
	#margen =
	#lomo =
	#ganancia =
	#tiempoImpresion =
	#tiempoEncuadernacion =
	#tiempoBN =
	#tiempoColor = 
	#tiempoXeikon =
	#tiempoTotal =
	#Papel1 =
	#Papel2 =
	#cantidad1 =
	#cantidad2 =
	#papelPortada =
	#cantidadPortada =
	cancelado = models.BooleanField(default=False)


	def __str__(self):
		return str(self.parte)


	class Meta:
		ordering = ('parte',)


	
	