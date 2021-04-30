from django.contrib import admin

from HeroicaTour_DB.models import SitioTuristico
from HeroicaTour_DB.models import Tour
from HeroicaTour_DB.models import Restaurante
from HeroicaTour_DB.models import Auto
from HeroicaTour_DB.models import Hotel
from HeroicaTour_DB.models import Trabajador
from HeroicaTour_DB.models import Cliente
from HeroicaTour_DB.models import Preferencia
from HeroicaTour_DB.models import Reseña
from HeroicaTour_DB.models import Taxi

admin.site.register(SitioTuristico)
admin.site.register(Tour)
admin.site.register(Restaurante)
admin.site.register(Auto)
admin.site.register(Hotel)
admin.site.register(Trabajador)
admin.site.register(Cliente)
admin.site.register(Preferencia)
admin.site.register(Reseña)
admin.site.register(Taxi)