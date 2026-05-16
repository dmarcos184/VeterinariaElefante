from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    def __str__(self): return self.nombre
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    def __str__(self): return self.nombre
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self): return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    def __str__(self): return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    def __str__(self): return self.nombre