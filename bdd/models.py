from django.db import models
from django.urls import reverse
from django.contrib import admin


"""
Marque
#######
id
label
"""


class Marque(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=56)


class Prix(models.Model):
    id = models.IntegerField(primary_key=True)
    id_voiture = models.IntegerField()
    prix = models.FloatField(max_length=56)
    date_start = models.DateField()
    date_stop = models.DateField(null=True, blank=True)

    class Meta():
        verbose_name = "Prix"
        verbose_name_plural = "Prix"


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


"""
Client
#######
id
nom
prenom
email
no_tel
ville
rue
code_postale
"""


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=56)
    prenom = models.CharField(max_length=56)
    email = models.CharField(max_length=56)
    no_tel = models.CharField(max_length=56)
    ville = models.CharField(max_length=56)
    rue = models.CharField(max_length=56)
    code_postale = models.CharField(max_length=56)


class ClientAdmin(admin.ModelAdmin):
    list_display = ("prenom","nom")


"""
Role
#######
id
titre
descri!ption
"""


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=56)
    description = models.CharField(max_length=56)

class RoleAdmin(admin.ModelAdmin):
    list_display = ("id","titre","description")


"""
Employee
#######
id
nom
prenom
email
no_tel
id_role
"""


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=56)
    prenom = models.CharField(max_length=56)
    email = models.CharField(max_length=56)
    no_tel = models.CharField(max_length=56)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("prenom","nom","email","no_tel")


"""
Commande
#######.
id
id_employee
id_client
date_commande
"""


class Commande(models.Model):
    id = models.IntegerField(primary_key=True)
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateField(null=True, blank=True)

class CommandeAdmin(admin.ModelAdmin):
    list_display = ("id","id_employee","id_client","date_commande")
