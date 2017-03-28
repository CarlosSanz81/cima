from django.contrib import admin
from .models import Acabado


# Register your models here.
@admin.register(Acabado)
class AdminAcabado(admin.ModelAdmin):
	list_display = ('nombre','coste','grosor',)

