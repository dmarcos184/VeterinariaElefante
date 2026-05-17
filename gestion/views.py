from django.shortcuts import render
from .models import Sucursal, Producto, Servicio, Doctor, Empleado

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'doctores.html', {'doctores': doctores})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales.html', {'sucursales': sucursales})

def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, {'empleados': empleados})

def ppagina1(request):
    return render(request, "ppagina1.html")

def ppagina2(request):
    return render(request, "ppagina2.html")

def ppagina3(request):
    return render(request, "ppagina3.html")

def ppagina4(request):
    return render(request, "ppagina4.html")