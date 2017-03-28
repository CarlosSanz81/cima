from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Modo(models.Model):
    nombre = models.CharField(max_length=100)
    colorPlano = models.BooleanField(default=False)
    bnPlano = models.BooleanField(default=False)
    ColorBnPlano = models.BooleanField(default=False)
    hibridoPlano = models.BooleanField(default=False)
    hibridoBobina = models.BooleanField(default=False)
    hibridoBobinaTom = models.BooleanField(default=False)
    colorBobina = models.BooleanField(default=False)
    colorBobinaTom = models.BooleanField(default=False)
    bnBobina = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre


    class Meta:
        ordering = ('nombre',)