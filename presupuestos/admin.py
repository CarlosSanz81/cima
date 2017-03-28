from django.contrib import admin
from .models import Parte


# Register your models here.
@admin.register(Parte)
class AdminPresupuestos(admin.ModelAdmin):
	list_display = ('parte','cliente','titulo','numeroCliente',)