from __future__ import unicode_literals

from django.db import models
from comercial.models import Comercial

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    numeroCliente = models.IntegerField(unique=True)
    Contacto = models.CharField(max_length=50, blank=True, null=True)
    Telefono = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    Email = models.EmailField(max_length=255, blank=True, null=True)
    comercial = models.ForeignKey(Comercial)

    def __str__(self):
        return self.nombre
        

    class Meta:
        ordering = ('nombre',)