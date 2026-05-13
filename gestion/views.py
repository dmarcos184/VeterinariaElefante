from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctores(request):
    return render(request, 'doctores.html')

def servicios(request):
    return render(request, 'servicios.html')

def productos(request):
    return render(request, 'productos.html')

def sucursales(request):
    return render(request, 'sucursales.html')