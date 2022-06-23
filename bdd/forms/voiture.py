from django.forms import ModelForm
from bdd.models.Voiture import Voiture


class VoitureForm(ModelForm):
    class Meta:
        model = Voiture
        fields = {"modele", "photo", "annee", "id_marque", "prix","pk_acheteur"}