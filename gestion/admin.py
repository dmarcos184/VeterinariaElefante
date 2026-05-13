from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sucursal, Doctor, Servicio, Producto, Empleado

admin.site.register(Sucursal)
admin.site.register(Doctor)
admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Empleado)   