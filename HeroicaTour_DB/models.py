from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

# Create your models here.
class Cliente(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    Nombre = models.CharField(max_length=25, null=False)
    Apellidos = models.CharField(max_length=25, null=False)
    Nacionalidad = models.CharField(max_length=25, null=False)
    Celular = models.CharField(max_length=15)
    Encuesta = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.Usuario) 
    
class Preferencia(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    Presupuesto = MoneyField(max_digits=10, default_currency='COP')
    Acompañantes = models.IntegerField(null=False)
    Alojamiento = models.BooleanField(default=False)
    Auto = models.BooleanField(default=False)
    Playa = models.BooleanField(default=False)
    Historia = models.BooleanField(default=False)
    Recordatorio = models.BooleanField(default=False)
    Duracion = models.IntegerField(null=False)
    
    def __str__(self):
        return str(self.Usuario) 

class Trabajador(models.Model):
    Guia = 'Guia'
    Soporte = 'Soporte'
    Admin = 'Admin'
    rol = [
        (Guia,'Guia'),
        (Soporte,'Soporte'),
        (Admin, 'Admin'),
    ]
    Nombre = models.CharField(max_length=25, null=False)
    Apellidos = models.CharField(max_length=25, null=False)
    Email = models.EmailField(max_length=25, null=False)
    Celular = models.CharField(max_length=15)
    CostoPerDay = MoneyField(max_digits=10, default_currency='COP')
    Rate = models.DecimalField(decimal_places=1, max_digits=5, default=5)
    Rol = models.CharField(max_length=25, choices=rol, default=None)
    Image = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.Nombre)

class ResenaTrabajador(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class SitioTuristico(models.Model):
    CentroComercial = 'Centros Comerciales'
    Playas = 'Playas'
    Turistico = 'Turistico'
    Centro = 'Centro Historico'
    categoriast = [
        (CentroComercial,'Centros Comerciales'),
        (Playas,'Playas'),
        (Turistico, 'Turistico'),
        (Centro, 'Centro Historico'),
    ]
    Nombre = models.CharField(max_length=25, null=False)
    Direccion = models.CharField(max_length=25, null=False)
    Latitud = models.FloatField(null=False)
    Longitud = models.FloatField(null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, default=5)
    CostoEntrada = MoneyField(max_digits=10, default_currency='COP')
    Categoria = models.CharField(max_length=25, choices=categoriast, default=None)
    Descripcion = models.TextField(max_length=2000)
    Image = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.Nombre)
    
class ResenaSitio(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    SitioTuristico = models.ForeignKey(SitioTuristico, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Tour(models.Model):
    Playas = 'Playas'
    CentroComercial = 'Centros Comerciales'
    HistoriaCultura = 'Historia y Cultura'
    Diversion = 'Diversion'
    categoriat = [
        (Playas,'Playas'),
        (CentroComercial,'Centros Comerciales'),
        (HistoriaCultura, 'Historia y Cultura'),
        (Diversion, 'Diversion'),
    ]
    Nombre = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, choices=categoriat, default=None)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, default=5)
    Descripcion = models.TextField(max_length=2000)
    Costo = MoneyField(max_digits=10, default_currency='COP')
    Duracion = models.IntegerField(null=False)
    Image = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.Nombre)

class ResenaTour(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Restaurante(models.Model):
    Corriente = 'Corrientes'
    Carnes = 'Restaurante de Carnes'
    Mar = 'Comida de Mar'
    Arabe = 'Comida Arabe'
    Fritos = 'Fritos'
    Colombiana = 'Comida Colombiana'
    categoriar = [
        (Corriente, 'Corrientes'),
        (Carnes, 'Restaurante de Carnes'),
        (Mar, 'Comida de Mar'),
        (Arabe, 'Comida Arabe'),
        (Fritos, 'Fritos'),
        (Colombiana, 'Comida Colombiana'),
    ]
    Nombre = models.CharField(max_length=25, null=False)
    Direccion = models.CharField(max_length=25, null=False)
    Latitud = models.FloatField(null=False)
    Longitud = models.FloatField(null=False)
    Categoria = models.CharField(max_length=25, choices = categoriar, default=None)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, default=5)
    CostoMin = MoneyField(max_digits=10, default_currency='COP')
    CostoMax = MoneyField(max_digits=10, default_currency='COP')
    Descripcion = models.TextField(max_length=2000)
    Image = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.Nombre)

class ResenaRestaurante(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Hotel(models.Model):
    Lujoso = 'Lujoso'
    Modesto = 'Modesto'
    Noche = 'Solo pasar la noche'
    categoriah = [
        (Lujoso,'Lujoso'),
        (Modesto,'Modesto'),
        (Noche, 'Solo pasar la noche'),
    ]
    Nombre = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, default=5)
    Direccion = models.CharField(max_length=25, null=False)
    Latitud = models.FloatField(null=False)
    Longitud = models.FloatField(null=False)
    Categoria = models.CharField(max_length=25, choices = categoriah, default=None)
    Telefono = models.CharField(max_length=10, null=True)
    Descripcion = models.TextField(max_length=2000)
    Web = models.CharField(max_length=25, null=False)
    Image = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.Nombre)

class ResenaHotel(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Auto(models.Model):
    Rojo = 'Rojo'
    Gris = 'Gris'
    Negro = 'Negro'
    Blanco = 'Blanco'
    Amarillo = 'Amarillo'
    Azul = 'Azul'
    Verde = 'Verde'
    Naranja = 'Naranja'
    Morado = 'Morado'
    color = [
        (Rojo, 'Rojo'),
        (Gris, 'Gris'),
        (Negro, 'Negro'),
        (Blanco, 'Blanco'),
        (Amarillo, 'Amarillo'),
        (Azul, 'Azul'),
        (Verde, 'Verde'),
        (Naranja, 'Naranja'),
        (Morado, 'Morado'),
    ]
    Matricula = models.CharField(max_length=25)       
    Marca = models.CharField(max_length=255)
    Modelo = models.CharField(max_length=255)
    Color =  models.CharField(max_length=25, choices=color, default=None)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, default=5)
    Capacidad = models.IntegerField(null=False)
    CostoPerDay = MoneyField(max_digits=10, default_currency='COP')
    Descripcion = models.TextField(max_length=2000)
    Image = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.Matricula)

class ResenaAuto(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Auto = models.ForeignKey(Auto, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Souvenir(models.Model):
    Nombre = models.CharField(max_length=25)
    LugardeVenta = models.CharField(max_length=25)
    CostoMin = MoneyField(max_digits=10, default_currency='COP')
    costoMax = MoneyField(max_digits=10, default_currency='COP')
    Descripcion = models.TextField(max_length=2000)
    Image = models.CharField(max_length=255, null=False)   
    
    def __str__(self):
        return str(self.Nombre)
    
class ResenaSouvenir(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Souvenir = models.ForeignKey(Souvenir, on_delete=models.CASCADE, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=5, null=False)
    Descripcion = models.TextField(max_length=500)

class Taxi(models.Model):
    Barrio = models.CharField(max_length=25, null=False, primary_key=True)
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
    PlayaBlanca = MoneyField(max_digits=10, default_currency='COP')
    Baru = MoneyField(max_digits=10, default_currency='COP')
    Aeropuerto = MoneyField(max_digits=10, default_currency='COP')
    Terminal = MoneyField(max_digits=10, default_currency='COP')
    
    def __str__(self):
        return str(self.Barrio)