from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctores/', views.doctores, name='doctores'),
    path('servicios/', views.servicios, name='servicios'),
    path('productos/', views.productos, name='productos'),
    path('sucursales/', views.sucursales, name='sucursales'),
]