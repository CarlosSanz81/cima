from django.contrib import admin
from .models import CodigosPostales


# Register your models here.
@admin.register(CodigosPostales)
class AdminCodpostal(admin.ModelAdmin):
	list_display = ('codigoPostal','Poblacion',)