from django.contrib import admin
from .models import FormaDePago

@admin.register(FormaDePago)
class AdminFormaDePago(admin.ModelAdmin):
	list_display = ('nombre','prioridad','dias')