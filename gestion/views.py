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
def ppagina1(request):
    return render(request, "ppagina1.html")

def ppagina2(request):
    return render(request, "ppagina2.html")

def ppagina3(request):
    return render(request, "ppagina3.html")

def ppagina4(request):
    return render(request, "ppagina4.html")