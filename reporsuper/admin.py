from django.contrib import admin
from .models import Instalacion, Puesto, Empleado, Supervision
# Register your models here.

admin.site.register(Instalacion)
admin.site.register(Puesto)
admin.site.register(Empleado)
admin.site.register(Supervision)