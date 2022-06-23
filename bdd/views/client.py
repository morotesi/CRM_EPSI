from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import  Paginator, EmptyPage
from bdd.models.Client import Client
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from bdd.forms.client import ClientForm

@login_required
def client_list(request):
    selected="clients"
    client_list= Client.objects.all()

    #pagination pour nbre d'elements par page
    paginator = Paginator(client_list.order_by('-date_mise_a_jour'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        client_list = paginator.page(page)
    except EmptyPage:
        client_list = paginator.page(paginator.num_pages())
    return render(request, "client/client_list.html", locals())



class CreateClient(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    template_name = "client/client_form.html"

    def get_success_url(self):
        return reverse_lazy("client_detail", kwargs={"pk": self.object.id})


class UpdateClient(UpdateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    template_name = "client/client_form.html"

    def get_success_url(self):
        return reverse_lazy("client_detail", kwargs={"pk": self.object.id})
