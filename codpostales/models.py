from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CodigosPostales(models.Model):
    codigoPostal = models.IntegerField(unique=True)
    Poblacion = models.CharField(max_length=255)

    def __str__(self):
        return self.Poblacion


    class Meta:
        ordering = ('codigoPostal',)