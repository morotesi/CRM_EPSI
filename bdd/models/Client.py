from django.core.validators import RegexValidator
from django.db import models

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
    date_mise_a_jour = models.DateField(verbose_name="Date de mise à jour", auto_now=True)
    nom = models.CharField(max_length=56)
    prenom = models.CharField(max_length=56)
    email = models.EmailField(max_length=56)
    no_tel_regex=RegexValidator(
        regex="[0-9]{10}", message="veuillez entrer un numéro de téléphone valide."
    )
    no_tel = models.CharField(validators=[no_tel_regex], max_length=10)
    ville = models.CharField(max_length=56)
    rue = models.CharField(max_length=56)
    code_postale_regex = RegexValidator(
        regex="[0-9]*$", message="veuillez entrer un code postal valide."
    )
    code_postale = models.CharField(max_length=56)
    date_inscription = models.DateField(verbose_name="Date d'inscription", auto_now_add=True)

    def get_adresse_complete_str(self):
        return f"{self.rue} \n {self.ville}{self.code_postale}"
