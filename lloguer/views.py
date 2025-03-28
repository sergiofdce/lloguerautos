from django.shortcuts import render
from lloguer.models import Automobil

# lloguer/views.py
def listar_automoviles(request):
    automoviles = Automobil.objects.all()
    return render(request, 'lloguer/listar_automoviles.html', {'automoviles': automoviles})
