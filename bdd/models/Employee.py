from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import  receiver

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_tel_regex = RegexValidator(
        regex="[0-9]{10}", message="veuillez entrer un numéro de téléphone valide."
    )
    no_tel = models.CharField(validators=[no_tel_regex], max_length=10, blank=True)
    rue = models.CharField(max_length=56, blank=True)
    ville = models.CharField(max_length=56, blank=True)
    code_postale_regex = RegexValidator(
        regex="[0-9]*$", message="veuillez entrer un code postal valide."
    )
    code_postale = models.CharField(max_length=56, blank=True)

    def get_adresse_complete_str(self):
        return f"{self.user.employee.rue} \n {self.user.employee.ville}{self.user.employee.code_postale}"

    def __str__(self):
        return self.user.username








