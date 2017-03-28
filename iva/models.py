from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Iva(models.Model):
    tipo = models.DecimalField(max_digits=2, decimal_places=0, unique=True)

    def __str__(self):
        return str(self.tipo)


    class Meta:
        ordering = ('tipo',)