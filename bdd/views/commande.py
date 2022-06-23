from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from bdd.forms.commande import CommandeForm
from bdd.models.Commande import Commande
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


# Create your views here.
@login_required
def index(request):
    commandes = Commande.objects.all()

    return render(request, 'commande/commande_list.html',context={"commandes": commandes})

@login_required
def commande_details(request, id):
    commande = get_object_or_404(Commande, id=id)

    return render(request, 'commande/commande_details.html', context={"commande": commande})

class CreateCommande(CreateView, LoginRequiredMixin):
    model = Commande
    form_class = CommandeForm
    template_name = "commande/commande_form.html"




    def get_success_url(self):
        return reverse_lazy("commande_detail", kwargs={"pk": self.object.id})


class UpdateCommande(UpdateView, LoginRequiredMixin):
    model = Commande
    form_class = CommandeForm
    template_name = "commande/commande_form.html"

    def get_success_url(self):
        return reverse_lazy("commande_detail", kwargs={"pk": self.object.id})
