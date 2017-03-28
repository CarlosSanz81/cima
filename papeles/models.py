from __future__ import unicode_literals

from django.db import models
from proveedor.models import Proveedor
from gramajes.models import Gramaje

# Create your models here.
class Papel(models.Model):
    nombre = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor)
    referencia = models.CharField(max_length=50, blank=True)
    gramaje = models.ForeignKey(Gramaje)
    mano = models.DecimalField(max_digits=3, decimal_places=2)
    precioTonelada = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)
