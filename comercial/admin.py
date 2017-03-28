from django.contrib import admin
from .models import Comercial


# Register your models here.
@admin.register(Comercial)
class AdminComercial(admin.ModelAdmin):
	list_display = ('nombre','Telefono', 'Email',)