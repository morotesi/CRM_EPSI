from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from bdd.forms.voiture import VoitureForm
from django.contrib.auth.models import Permission
from bdd.models.Voiture import Voiture
from bdd.models.Employee import Employee
from bdd.models.Marque import Marque
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


@login_required
def index(request):
    voitures = Voiture.objects.all()
    marques = Marque.objects.all()
    user = request.user

    return render(request, 'vitrine/home.html',context={"voitures": voitures, "marques":marques , "username": user.username})

@login_required
def voiture_details(request, id):
    voiture = get_object_or_404(Voiture, id=id)

    return render(request, 'vitrine/voiture_details.html', context={"voiture": voiture})

class CreateVoiture(CreateView, LoginRequiredMixin):
    model = Voiture
    form_class = VoitureForm
    template_name = "vitrine/voiture_form.html"

    def get_success_url(self):
        return reverse_lazy("voiture_detail", kwargs={"pk": self.object.id})


class UpdateVoiture(UpdateView, LoginRequiredMixin):
    model = Voiture
    form_class = VoitureForm
    template_name = "vitrine/voiture_form.html"

    def get_success_url(self):
        return reverse_lazy("voiture_detail", kwargs={"pk": self.object.id})