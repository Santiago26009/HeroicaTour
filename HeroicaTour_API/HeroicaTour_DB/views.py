from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

# Create your views here.
class ClTrabajadorView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Trabajador
    queryset = modeltrabajador.objects.all()
    
class ClClienteView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Cliente
    queryset = modelcliente.objects.all()

class ClAutoView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Auto
    queryset = modelauto.objects.all()
    
class ClSitioView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Sitio
    queryset = modelsitio.objects.all()
    
class ClTourView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Tour
    queryset = modeltour.objects.all()
    
class ClRestView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Rest
    queryset = modelrest.objects.all()
    
class ClHotelView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Hotel
    queryset = modelhotel.objects.all()
    
class ClTaxiView(ListAPIView, CreateAPIView):
    serializer_class = serializer.CS_Taxi
    queryset = modeltaxi.objects.all()


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

class AdClienteView(ListAPIView, CreateAPIView):
    serializer_class = serializer.AS_Cliente
    queryset = modelcliente.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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