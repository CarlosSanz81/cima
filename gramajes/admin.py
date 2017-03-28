from django.contrib import admin
from .models import Gramaje

@admin.register(Gramaje)
class AdminGramaje(admin.ModelAdmin):
	list_display = ('gramaje',)