from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Trabajador, Usuario, Auto, SitioTuristico, Tour, Restaurante, Hotel, Taxi, Souvenir, Preferencia

class CS_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ['Nombre','Apellidos','Rate','Celular']

class AS_Trabajador(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('__all__')

class CS_Usuario(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','Email','Usuario','Password','Nombre','Apellidos','Nacionalidad','Celular']

class AS_Usuario(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','Usuario','Nombre','Apellidos','Nacionalidad','Celular','Email','Encuesta']

class CS_Auto(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['Matricula','Marca','Modelo', 'Color', 'Rate','Capacidad','CostoPerDay','Descripcion', 'Image'] 

class AS_Auto(serializers.ModelSerializer): 
    class Meta:
        model = Auto
        fields = ('__all__')
        
class CS_Sitio(serializers.ModelSerializer):
    class Meta:
        model = SitioTuristico
        fields = ['Nombre','Direccion','Rate','CostoEntrada','Categoria','Descripcion','Image']

class AS_Sitio(serializers.ModelSerializer):
    class Meta:
        model = SitioTuristico
        fields = ('__all__')
        
class CS_Tour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['Nombre','Categoria','Rate','Descripcion','Costo','Duracion','Image']
        
class AS_Tour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('__all__')
        
class CS_Rest(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['Nombre','Direccion','Categoria','Rate','CostoMin','CostoMax','Descripcion','Image']
        
class AS_Rest(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('__all__')
        
class CS_Hotel(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['Nombre','Rate','Direccion','Categoria','Telefono','Web','Image']
        
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
        fields = ['Nombre','LugardeVenta','CostoMin','CostoMax','Image']
        
class AS_Souvenir(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = ('__all__')

class CS_Preferencia(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = ['Cliente','Presupuesto','Acompañantes','Alojamiento', 'Auto','Playa','Historia','Recordatorio','Duracion']
        
class AS_Preferencia(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = ('__all__')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'Usuario', 'Email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','Email','Usuario','Password','Nombre','Apellidos','Nacionalidad','Celular')
        extra_kwargs = {'Password': {'write_only': True}}

    def post(self, validated_data):
        user = self.create(validated_data['Usuario'], validated_data['Email'], validated_data['Password'],validated_data['Nombre'], validated_data['Apellidos'], validated_data['Nacionalidad'], validated_data['Celular'])
        return user
