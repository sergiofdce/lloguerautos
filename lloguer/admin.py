from django.contrib import admin
from lloguer.models import *


# Register your models here.

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')
    search_fields = ('matricula', 'marca', 'model')
    list_filter = ('marca',)

admin.site.register(Automobil, AutomobilAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'user', 'data_inici', 'data_fi')
    search_fields = ('automobil__matricula', 'user__username', 'data_inici')
    list_filter = ('automobil', 'data_inici')

admin.site.register(Reserva, ReservaAdmin)