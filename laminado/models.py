from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TipoLaminado(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    coste = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)