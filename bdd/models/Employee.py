from django.db import models
from django.contrib import admin


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
    role = models.CharField(max_length=20)


role = {"ADMIN_ROLE", "CUSTOMER_ROLE", "BUYER_ROLE"}

