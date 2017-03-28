from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class AdminProveedor(admin.ModelAdmin):
	list_display = ('nombre',)