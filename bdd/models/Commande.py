from django.db import models
from bdd.models.Employee import Employee
from bdd.models.Client import Client
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
