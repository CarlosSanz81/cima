from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Transporte(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)
