"""HeroicaTour_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HeroicaTour_DB import views
from knox import views as knox_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('register/', views.RegisterAPI.as_view()),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
    path('cl/trabajadores/', views.ClTrabajadorView.as_view()),
    path('ad/trabajadores/', views.AdTrabajadorView.as_view()),
    path('ad/trabajadores/<int:pk>', views.AdTrabajadorViewDetails.as_view()),
    
    path('cl/clientes/', views.ClClienteView.as_view()),
    path('cl/clientes/<int:pk>', views.ClClienteViewDetails.as_view()),
    path('ad/clientes/', views.AdClienteView.as_view()),
    path('ad/clientes/<int:pk>', views.AdClienteViewDetails.as_view()),
    
    path('cl/autos/', views.ClAutoView.as_view()),
    path('ad/autos/', views.AdAutoView.as_view()),
    path('ad/autos/<int:pk>', views.AdAutoViewDetails.as_view()),
    
    path('cl/sitios/', views.ClSitioView.as_view()),
    path('ad/sitios/', views.AdSitioView.as_view()),
    path('ad/sitios/<int:pk>', views.AdSitioViewDetails.as_view()),
    
    path('cl/tours/', views.ClTourView.as_view()),
    path('ad/tours/', views.AdTourView.as_view()),
    path('ad/tours/<int:pk>', views.AdTourViewDetails.as_view()),
    
    path('cl/restaurantes/', views.ClRestView.as_view()),
    path('ad/restaurantes/', views.AdRestView.as_view()),
    path('ad/restaurantes/<int:pk>', views.AdRestViewDetails.as_view()),
    
    path('cl/hoteles/', views.ClHotelView.as_view()),
    path('ad/hoteles/', views.AdHotelView.as_view()),
    path('ad/hoteles/<int:pk>', views.AdHotelViewDetails.as_view()),
    
    path('cl/taxi/', views.ClTaxiView.as_view()),
    path('ad/taxi/', views.AdTaxiView.as_view()),
    path('ad/taxi/<int:pk>', views.AdTaxiViewDetails.as_view()),
    
    path('cl/souvenir/', views.ClSouvenirView.as_view()),
    path('ad/souvenir/', views.AdSouvenirView.as_view()),
    path('ad/souvenir/<int:pk>', views.AdSouvenirViewDetails.as_view()),
    
    path('cl/preferencias/', views.ClPreferenciaView.as_view()),
    path('cl/preferencias/<int:pk>', views.ClPreferenciaViewDetails.as_view()),
    path('ad/preferencias/', views.AdPreferenciaView.as_view()),
    path('ad/preferencias/<int:pk>', views.AdPreferenciaViewDetails.as_view()),
    
    path('cl/encuesta/trabajador/', views.ClResenaTrabajadorView.as_view()),
    path('cl/encuesta/sitio/', views.ClResenaSitioView.as_view()),
    path('cl/encuesta/tour/', views.ClResenaTourView.as_view()),
    path('cl/encuesta/restaurante/', views.ClResenaRestauranteView.as_view()),
    path('cl/encuesta/hotel/', views.ClResenaHotelView.as_view()),
    path('cl/encuesta/auto/', views.ClResenaAutoView.as_view()),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
