from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Gramaje(models.Model):
    gramaje = models.IntegerField(unique=True)
    
    def __str__(self):
        return str(self.gramaje)


    class Meta:
        ordering = ('gramaje',)
