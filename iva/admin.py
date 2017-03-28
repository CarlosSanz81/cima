from django.contrib import admin
from .models import Iva

@admin.register(Iva)
class AdminIva(admin.ModelAdmin):
	list_display = ('tipo',)