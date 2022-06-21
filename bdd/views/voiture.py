from django.shortcuts import render

# Create your views here.
from bdd.models.Voiture import Voiture


def index(request):
    voitures = Voiture.objects.all()

    return render(request, 'vitrine/index.html',context={"voitures": voitures})