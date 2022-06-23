from django.db import models
from bdd.models.Employee import Employee
from bdd.models.Client import Client
"""
Commande
#######.
id
id_employee1
id_client
date_commande
"""


class Commande(models.Model):
    id_employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    id_client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_commande = models.DateField(verbose_name="Date de validation de la commande", auto_now_add=True)
