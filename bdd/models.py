from django.db import models
from django.urls import reverse
from django.contrib import admin







"""
Voiture
#######
id
id_marque
modele
photo
annee
date_entree
date_sortie
id_acheteur
prix
"""


class Voiture(models.Model):
    id = models.IntegerField(primary_key=True)
    id_marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    modele = models.CharField(max_length=56)
    photo = models.ImageField(upload_to="voitures", blank=True, null=True)
    annee = models.IntegerField()
    date_entree = models.DateField()
    date_sortie = models.DateField(null=True, blank=True)
    id_acheteur = models.IntegerField()
    prix = models.ForeignKey(Prix, on_delete=models.PROTECT)

    def __str__(self):
        return self.modele

    def get_absolute_url(self):
        return reverse("voiture", kwargs={"id": self.id})










