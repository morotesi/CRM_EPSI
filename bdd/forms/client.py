from django.forms import ModelForm
from bdd.models.Client import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = {"nom", "prenom", "email", "no_tel", "ville", "rue", "code_postale"}