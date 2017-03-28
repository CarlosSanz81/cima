from django.contrib import admin
from .models import Papel

@admin.register(Papel)
class AdminPapel(admin.ModelAdmin):
	list_display = ('nombre',)