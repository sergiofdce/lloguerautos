from django.contrib import admin
from lloguer.models import *


# Register your models here.

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')
    search_fields = ('matricula', 'marca', 'model')
    list_filter = ('marca',)

admin.site.register(Automobil, AutomobilAdmin)

