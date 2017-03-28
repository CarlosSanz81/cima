from django.contrib import admin
from .models import Clientes


# Register your models here.
@admin.register(Clientes)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre','numeroCliente','Contacto', 'Telefono', 'Email')
# Register your models here.
