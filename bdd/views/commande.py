from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from bdd.forms.commande import CommandeForm
from bdd.models.Commande import Commande
from bdd.models.Voiture import Voiture
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


# Create your views here.
@login_required
def index(request):
    commande_list = Commande.objects.all()

    # pagination pour nbre d'elements par page
    paginator = Paginator(commande_list.order_by('-date_commande'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        commande_list = paginator.page(page)
    except EmptyPage:
        commande_list = paginator.page(paginator.num_pages())
    return render(request, 'commande/commande_list.html',context={"commande_list": commande_list})

@login_required
def commande_details(request, id):
    commande = get_object_or_404(Commande, id=id)
    id_voiture = request.query_params.get('pk')
    print(id_voiture)
    return render(request, 'commande/commande_details.html', context={"commande": commande})



class CreateCommande(CreateView, LoginRequiredMixin):
    model = Commande
    form_class = CommandeForm
    template_name = "commande/commande_form.html"




    def get_success_url(self):
        employee = request.user
        return reverse_lazy("commande_detail", kwargs={"pk": self.object.id})


class UpdateCommande(UpdateView, LoginRequiredMixin):
    model = Commande
    form_class = CommandeForm
    template_name = "commande/commande_form.html"

    def get_success_url(self):
        return reverse_lazy("commande_detail", kwargs={"pk": self.object.id})
