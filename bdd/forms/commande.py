from django.forms import ModelForm
from bdd.models.Commande import Commande


class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = {"pk_employee", "pk_client"}