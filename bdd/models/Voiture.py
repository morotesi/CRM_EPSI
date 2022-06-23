from django.db import models
from django.urls import reverse
from bdd.models.Marque import Marque
from bdd.models.Employee import Employee



class Voiture(models.Model):
    id_marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    modele = models.CharField(max_length=56)
    photo = models.ImageField(upload_to="voitures", blank=True, null=True)
    annee = models.IntegerField()
    date_entree = models.DateField(verbose_name="Date d'entrée au catalogue", auto_now_add=True)
    date_sortie = models.DateField(null=True, blank=True)
    pk_acheteur = models.ForeignKey(Employee, null=True, default=None, on_delete=models.CASCADE, related_name="employee")
    prix = models.FloatField()

    def __str__(self):
        return self.modele

    def get_absolute_url(self):
        return reverse("voiture", kwargs={"pk": self.pk})