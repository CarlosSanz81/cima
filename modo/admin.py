from django.contrib import admin
from .models import Modo

@admin.register(Modo)
class AdminModo(admin.ModelAdmin):
	list_display = ('nombre',)