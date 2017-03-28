from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comercial(models.Model):
    nombre = models.CharField(max_length=100)
    Telefono = models.DecimalField(max_digits=9, decimal_places=0,unique=True)
    Email = models.EmailField(max_length=255)
 
    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)