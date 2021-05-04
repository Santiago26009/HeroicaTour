from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Trabajador(models.Model):
    Usuario = models.CharField(max_length=25)
    Password = models.CharField(max_length=25, null=False)
    Nombre = models.CharField(max_length=25, null=False)
    Apellidos = models.CharField(max_length=25, null=False)
    Celular = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254)
    Rate = models.DecimalField(decimal_places=1, max_digits=5)
    Rol = models.CharField(max_length=25)

class SitioTuristico(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Direccion = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5)
    Costo = MoneyField(max_digits=10, default_currency='COP')
    Categoria = models.CharField(max_length=25, null=False)
    Descripcion = models.TextField(max_length=500)

class Tour(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5)
    Descripcion = models.TextField(max_length=500)
    Costo = MoneyField(max_digits=10, default_currency='COP')
    Duracion = models.IntegerField(null=False)

class Restaurante(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Direccion = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5)
    CostoMin = MoneyField(max_digits=10, default_currency='COP')
    CostoMax = MoneyField(max_digits=10, default_currency='COP')
    Descripcion = models.TextField(max_length=500)

class Auto(models.Model):
    Matricula = models.CharField(max_length=25)       
    Marca = models.CharField(max_length=255)
    Modelo = models.CharField(max_length=255)
    Rate = models.DecimalField(decimal_places=1, max_digits=5)
    Capacidad = models.IntegerField(null=False)
    CostoPerDay = MoneyField(max_digits=10, default_currency='COP')
    Descripcion = models.TextField(max_length=500)

class Hotel(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5)
    Direccion = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, null=False)
    Web = models.CharField(max_length=25, null=False)

class Taxi(models.Model):
    Barrio = MoneyField(max_digits=10, default_currency='COP')
    Centro = MoneyField(max_digits=10, default_currency='COP')
    Crespo = MoneyField(max_digits=10, default_currency='COP')
    Marbella = MoneyField(max_digits=10, default_currency='COP')
    Cabrero = MoneyField(max_digits=10, default_currency='COP')
    Bocagrande = MoneyField(max_digits=10, default_currency='COP')
    CastilloGrande = MoneyField(max_digits=10, default_currency='COP')
    ElLaguito = MoneyField(max_digits=10, default_currency='COP')
    LaBoquilla = MoneyField(max_digits=10, default_currency='COP')
    Manzanillo = MoneyField(max_digits=10, default_currency='COP')
    SanFelipe = MoneyField(max_digits=10, default_currency='COP')
    LaPopa = MoneyField(max_digits=10, default_currency='COP')
    Manga = MoneyField(max_digits=10, default_currency='COP')

class Cliente(models.Model):
    Usuario = models.CharField(max_length=25)
    Password = models.CharField(max_length=25, null=False)
    Nombre = models.CharField(max_length=25, null=False)
    Apellidos = models.CharField(max_length=25, null=False)
    Nacionalidad = models.CharField(max_length=25, null=False)
    Celular = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254)

class Reseña(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    Trabajador = models.ForeignKey(Trabajador, on_delete=models.SET_NULL, null=True)
    Tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    Hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    Restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, null=True)
    SitioTuristico = models.ForeignKey(SitioTuristico, on_delete=models.SET_NULL, null=True)
    Auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Preferencia(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    Presupuesto = MoneyField(max_digits=10, default_currency='COP')
    Acompañantes = models.IntegerField(null=False)
    Alojamiento = models.BooleanField(default=False)
    Auto = models.BooleanField(default=False)
    Duracion = models.IntegerField(null=False)
    
class Souvenir(models.Model):
    Nombre = models.CharField(max_length=25)
    LugardeVenta = models.CharField(max_length=25)
    CostoMin = MoneyField(max_digits=10, default_currency='COP')
    costoMax = MoneyField(max_digits=10, default_currency='COP')