from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Trabajador, Cliente, Auto, SitioTuristico, Tour, Restaurante, Hotel, Taxi, Souvenir, Preferencia, ResenaTrabajador, ResenaSitio, ResenaTour, ResenaRestaurante, ResenaHotel, ResenaAuto

class CS_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ['id','Nombre','Apellidos','Rate','Celular']

class AS_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('__all__')

class CS_Cliente(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['Usuario','Nombre','Apellidos','Nacionalidad','Celular']

class AS_Cliente(serializers.ModelSerializer):
    class Meta:
        model = Cliente 
        fields = ['id','Usuario','Nombre','Apellidos','Nacionalidad','Celular']

class CS_Auto(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['id','Matricula','Marca','Modelo', 'Color', 'Rate','Capacidad','CostoPerDay','Descripcion', 'Image'] 

class AS_Auto(serializers.ModelSerializer): 
    class Meta:
        model = Auto
        fields = ('__all__')
        
class CS_Sitio(serializers.ModelSerializer):
    class Meta:
        model = SitioTuristico
        fields = ['id','Nombre','Direccion','Latitud','Longitud','Rate','CostoEntrada','Categoria','Descripcion','Image']

class AS_Sitio(serializers.ModelSerializer):
    class Meta:
        model = SitioTuristico
        fields = ('__all__')
        
class CS_Tour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id','Nombre','Categoria','Rate','Descripcion','Costo','Duracion','Image']
        
class AS_Tour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('__all__')
        
class CS_Rest(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id','Nombre','Direccion','Latitud','Longitud','Categoria','Rate','CostoMin','CostoMax','Descripcion','Image']
        
class AS_Rest(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('__all__')
        
class CS_Hotel(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','Nombre','Rate','Direccion','Latitud','Longitud','Categoria','Telefono','Web','Image']
        
class AS_Hotel(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('__all__')

class CS_Taxi(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['Barrio','Centro','Crespo','Marbella','Cabrero','Bocagrande','CastilloGrande','ElLaguito','LaBoquilla','Manzanillo','SanFelipe','LaPopa','Manga', 'PlayaBlanca', 'Baru', 'Aeropuerto','Terminal']
        
class AS_Taxi(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['Barrio','Centro','Crespo','Marbella','Cabrero','Bocagrande','CastilloGrande','ElLaguito','LaBoquilla','Manzanillo','SanFelipe','LaPopa','Manga', 'PlayaBlanca', 'Baru', 'Aeropuerto','Terminal']
        
class CS_Souvenir(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = ['id','Nombre','LugardeVenta','CostoMin','CostoMax','Image']
        
class AS_Souvenir(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = ('__all__')

class CS_Preferencia(serializers.ModelSerializer):  
    class Meta:
        model = Preferencia
        fields = ['Usuario','Presupuesto','Acompañantes','Alojamiento', 'Auto','Playa','Historia','Recordatorio','Duracion']
        
class AS_Preferencia(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = ('__all__')

class R_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = ResenaTrabajador
        fields = ['Cliente','Trabajador','Rate','Descripcion']
        
class R_Sitio(serializers.ModelSerializer):
    class Meta:
        model = ResenaSitio
        fields = ['Cliente','SitioTuristico','Rate','Descripcion']
        
class R_Tour(serializers.ModelSerializer):
    class Meta:
        model = ResenaTour
        fields = ['Cliente','Tour','Rate','Descripcion']
        
class R_Rest(serializers.ModelSerializer):
    class Meta:
        model = ResenaRestaurante
        fields = ['Cliente','Restaurante','Rate','Descripcion']
        
class R_Hotel(serializers.ModelSerializer):
    class Meta:
        model = ResenaHotel
        fields = ['Cliente','Hotel','Rate','Descripcion']
        
class R_Auto(serializers.ModelSerializer):
    class Meta:
        model = ResenaAuto
        fields = ['Cliente','Auto','Rate','Descripcion']

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user