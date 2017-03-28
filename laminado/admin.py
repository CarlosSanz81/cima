from django.contrib import admin
from .models import TipoLaminado

@admin.register(TipoLaminado)
class AdminLaminado(admin.ModelAdmin):
	list_display = ('nombre',)
