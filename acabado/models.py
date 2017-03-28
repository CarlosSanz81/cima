from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Acabado(models.Model):
    nombre = models.CharField(max_length=100)
    coste = models.DecimalField(max_digits=6, decimal_places=3)
    grosor = models.DecimalField(max_digits=6, decimal_places=3, blank=True)

    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)