from rest_framework import serializers
from .models import Trabajador, Cliente, Auto, SitioTuristico, Tour, Restaurante, Hotel, Taxi

class CS_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ['Nombre','Apellidos','Email','Rate']

class AS_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ['id','Usuario','Nombre','Apellidos','Celular','Email','Rate','Rol']

class CS_Cliente(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')

class AS_Cliente(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','Usuario','Nombre','Apellidos','Nacionalidad','Celular','Email']

class CS_Auto(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['Matricula','Marca','Modelo','Rate','Capacidad','CostoPerDay','Descripcion'] 

class AS_Auto(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ('__all__')
        
class CS_Sitio(serializers.ModelSerializer):
    class Meta:
        model = SitioTuristico
        fields = ['Nombre','Direccion','Rate','Costo','Categoria','Descripcion']

class AS_Sitio(serializers.ModelSerializer):
    class Meta:
        model = SitioTuristico
        fields = ('__all__')
        
class CS_Tour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['Nombre','Categoria','Rate','Descripcion','Costo','Duracion']
        
class AS_Tour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('__all__')
        
class CS_Rest(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['Nombre','Direccion','Categoria','Rate','CostoMin','CostoMax','Descripcion']
        
class AS_Rest(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('__all__')
        
class CS_Hotel(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['Nombre','Rate','Direccion','Categoria','Web']
        
class AS_Hotel(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('__all__')

class CS_Taxi(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['Barrio','Centro','Crespo','Marbella','Cabrero','Bocagrande','CastilloGrande','ElLaguito','LaBoquilla','Manzanillo','SanFelipe','LaPopa','Manga']
        
class AS_Taxi(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['Barrio','Centro','Crespo','Marbella','Cabrero','Bocagrande','CastilloGrande','ElLaguito','LaBoquilla','Manzanillo','SanFelipe','LaPopa','Manga']