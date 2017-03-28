from __future__ import unicode_literals

from django.db import models
from formadepago.models import FormaDePago

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    numeroProveedor = models.IntegerField(unique=True)
    Contacto = models.CharField(max_length=50, blank=True)
    Telefono = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(max_length=255, blank=True)
    formaDePago = models.ForeignKey(FormaDePago)

    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)