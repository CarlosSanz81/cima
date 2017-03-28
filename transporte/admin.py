from django.contrib import admin
from .models import Transporte

@admin.register(Transporte)
class AdminTransporte(admin.ModelAdmin):
	list_display = ('nombre',)

