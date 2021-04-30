from django.db import models

# Create your models here.
class Trabajador(models.Model):
    Usuario = models.CharField(max_length=25, primary_key=True)
    Password = models.CharField(max_length=25, null=False)
    Nombre = models.CharField(max_length=25, null=False)
    Apellidos = models.CharField(max_length=25, null=False)
    Celular = models.IntegerField(null=False)
    Email = models.EmailField
    Rate = models.DecimalField(decimal_places=1, max_digits=1)
    Rol = models.CharField(max_length=25)

    def __str__(self):
        return f'Trabajador{self.Usuario} : {self.Nombre} {self.Apellidos}'

class SitioTuristico(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Direccion = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=1)
    Costo = models.IntegerField
    Categoria = models.CharField(max_length=25, null=False)
    Descripcion = models.TextField(max_length=500)

    def __str__(self):
        return f'SitioTuristico{self.id} : {self.Nombre} {self.Categoria}'

class Tour(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=1)
    Descripcion = models.TextField(max_length=500)
    Costo = models.IntegerField
    Duracion = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f'Tour{self.id} : {self.Nombre} {self.Categoria}'

class Restaurante(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Direccion = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=1)
    CostoMin = models.IntegerField
    CostoMax = models.IntegerField
    Descripcion = models.TextField(max_length=500)

    def __str__(self):
        return f'Restaurante{self.id} : {self.Nombre} {self.Categoria}'

class Auto(models.Model):
    Matricula = models.CharField(max_length=25, primary_key=True)
    Marca = models.CharField(max_length=255)
    Modelo = models.CharField(max_length=255)
    Rate = models.DecimalField(decimal_places=1, max_digits=1)
    Capacidad = models.IntegerField
    CostoPerDay = models.IntegerField
    Descripcion = models.TextField(max_length=500)

    def __str__(self):
        return f'Auto{self.Matricula} : {self.Marca} {self.Modelo}'

class Hotel(models.Model):
    Nombre = models.CharField(max_length=25, null=False)
    Rate = models.DecimalField(decimal_places=1, max_digits=1)
    Direccion = models.CharField(max_length=25, null=False)
    Categoria = models.CharField(max_length=25, null=False)
    Web = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f'Hotel{self.id} : {self.Nombre} {self.Web}'

class Taxi(models.Model):
    Barrio = models.CharField(max_length=255, primary_key=True)
    Centro = models.CharField(max_length=255)
    Crespo = models.CharField(max_length=255)
    Marbella = models.CharField(max_length=255)
    Cabrero = models.CharField(max_length=255)
    Bocagrande = models.CharField(max_length=255)
    CastilloGrande = models.CharField(max_length=255)
    ElLaguito = models.CharField(max_length=255)
    LaBoquilla = models.CharField(max_length=255)
    Manzanillo = models.CharField(max_length=255)
    SanFelipe = models.CharField(max_length=255)
    LaPopa = models.CharField(max_length=255)
    Manga = models.CharField(max_length=255)

    def __str__(self):
        return f'Taxi{self.Barrio}'

class Cliente(models.Model):
    Usuario = models.CharField(max_length=25, primary_key=True)
    Password = models.CharField(max_length=25, null=False)
    Nombre = models.CharField(max_length=25, null=False)
    Apellidos = models.CharField(max_length=25, null=False)
    Nacionalidad = models.CharField(max_length=25, null=False)
    Celular = models.IntegerField(null=False)
    Email = models.EmailField

    def __str__(self):
        return f'Cliente{self.Usuario} : {self.Nombre} {self.Apellidos}'

class Reseña(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    Trabajador = models.ForeignKey(Trabajador, on_delete=models.SET_NULL, null=True)
    Tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    Hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    Restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, null=True)
    SitioTuristico = models.ForeignKey(SitioTuristico, on_delete=models.SET_NULL, null=True)
    Auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)
    Rate = models.DecimalField(decimal_places=1, max_digits=1, null=False)
    Descripcion = models.TextField(max_length=500)

    def __str__(self):
        return f'Reseña{self.id} : {self.Cliente} {self.Rate}'

class Preferencia(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    Presupuesto = models.IntegerField(null=False)
    Acompañantes = models.IntegerField(null=False)
    Alojamiento = models.BooleanField(default=False)
    Auto = models.BooleanField(default=False)
    Duracion = models.IntegerField(null=False)

    def __str__(self):
        return f'Preferencia{self.id} : {self.Cliente}'