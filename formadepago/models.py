from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FormaDePago(models.Model):
    nombre = models.CharField(max_length=100)
    prioridad = models.IntegerField(unique=True)
    dias = models.IntegerField(unique=True)

    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)