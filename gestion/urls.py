from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctores/', views.doctores, name='doctores'),
    path('servicios/', views.servicios, name='servicios'),
    path('productos/', views.productos, name='productos'),
    path('sucursales/', views.sucursales, name='sucursales'),

    path("ppagina1/", views.ppagina1, name="ppagina1"),
    path("ppagina2/", views.ppagina2, name="ppagina2"),
    path("ppagina3/", views.ppagina3, name="ppagina3"),
    path("ppagina4/", views.ppagina4, name="ppagina4"),

]
