from django.shortcuts import render
from rest_framework.response import Response
from HeroicaTour_DB import serializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .models import Trabajador as modeltrabajador
from .models import Cliente as modelcliente
from .models import Auto as modelauto
from .models import SitioTuristico as modelsitio
from .models import Tour as modeltour
from .models import Restaurante as modelrest
from .models import Hotel as modelhotel
from .models import Taxi as modeltaxi
from .models import Souvenir as modelsouvenir
from .models import Preferencia as modelpreferencia
from .models import ResenaTrabajador as resenatrabajador
from. models import ResenaSitio as resenasitio
from. models import ResenaTour as resenatour
from. models import ResenaRestaurante as resenarestaurante
from. models import ResenaHotel as resenahotel
from. models import ResenaAuto as resenaauto
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.
class ClTrabajadorView(ListAPIView):
    serializer_class = serializer.CS_Trabajador
    queryset = modeltrabajador.objects.filter(Rol='Guia')
    
class ClClienteView(CreateAPIView):
    serializer_class = serializer.CS_Cliente
    queryset = modelcliente.objects.all()

class ClClienteViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.CS_Cliente
    queryset = modelcliente.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ClAutoView(ListAPIView):
    serializer_class = serializer.CS_Auto
    queryset = modelauto.objects.all()
    
class ClSitioView(ListAPIView):
    serializer_class = serializer.CS_Sitio
    queryset = modelsitio.objects.all()
    
class ClTourView(ListAPIView):
    serializer_class = serializer.CS_Tour
    queryset = modeltour.objects.all()
    
class ClRestView(ListAPIView):
    serializer_class = serializer.CS_Rest
    queryset = modelrest.objects.all()
    
class ClHotelView(ListAPIView):
    serializer_class = serializer.CS_Hotel
    queryset = modelhotel.objects.all()
    
class ClTaxiView(ListAPIView):
    serializer_class = serializer.CS_Taxi
    queryset = modeltaxi.objects.all()
    
class ClSouvenirView(ListAPIView):
    serializer_class = serializer.CS_Souvenir
    queryset = modelsouvenir.objects.all()

class ClPreferenciaView(CreateAPIView):
    serializer_class = serializer.CS_Preferencia
    queryset = modelpreferencia.objects.all()

class ClPreferenciaViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.CS_Preferencia
    queryset = modelpreferencia.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ClResenaTrabajadorView(CreateAPIView):
    serializer_class = serializer.R_Trabajador
    queryset = resenatrabajador.objects.all()

class ClResenaSitioView(CreateAPIView):
    serializer_class = serializer.R_Sitio
    queryset = resenasitio.objects.all()

class ClResenaTourView(CreateAPIView):
    serializer_class = serializer.R_Tour
    queryset = resenatour.objects.all()
    
class ClResenaRestauranteView(CreateAPIView):
    serializer_class = serializer.R_Rest
    queryset = resenarestaurante.objects.all()

class ClResenaHotelView(CreateAPIView):
    serializer_class = serializer.R_Hotel
    queryset = resenahotel.objects.all()

class ClResenaAutoView(CreateAPIView):
    serializer_class = serializer.R_Auto
    queryset = resenaauto.objects.all()

class AdTrabajadorView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Trabajador
    queryset = modeltrabajador.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdTrabajadorViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Trabajador
    queryset = modeltrabajador.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AdClienteView(ListAPIView):
    serializer_class = serializer.AS_Cliente
    queryset = modelcliente.objects.all()

class AdClienteViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Cliente
    queryset = modelcliente.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)     

class AdAutoView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Auto
    queryset = modelauto.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdAutoViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Auto
    queryset = modelauto.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
    
class AdSitioView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Sitio
    queryset = modelsitio.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdSitioViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Sitio
    queryset = modelsitio.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)   

class AdTourView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Tour
    queryset = modeltour.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdTourViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Tour
    queryset = modeltour.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  
    
class AdRestView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Rest
    queryset = modelrest.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdRestViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Rest
    queryset = modelrest.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  

class AdHotelView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Hotel
    queryset = modelhotel.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdHotelViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Hotel
    queryset = modelhotel.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class AdTaxiView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Taxi
    queryset = modeltaxi.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdTaxiViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Taxi
    queryset = modeltaxi.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AdSouvenirView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Souvenir
    queryset = modelsouvenir.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdSouvenirViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Souvenir
    queryset = modelsouvenir.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AdPreferenciaView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Preferencia
    queryset = modelpreferencia.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdPreferenciaViewDetails(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializer.AS_Preferencia
    queryset = modelpreferencia.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
