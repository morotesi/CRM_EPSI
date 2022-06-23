from django.db import models
from bdd.models.Employee import Employee
from bdd.models.Client import Client
from bdd.models.Voiture import Voiture
"""
Commande
#######.
id
id_employee1
id_client
date_commande
"""


class Commande(models.Model):
    pk_employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    pk_client = models.ForeignKey(Client, on_delete=models.PROTECT)
    id_voiture = models.ForeignKey(Voiture, on_delete=models.PROTECT)
    date_commande = models.DateField(verbose_name="Date de validation de la commande", auto_now_add=True)
