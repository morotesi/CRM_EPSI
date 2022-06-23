from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from mspr import settings
from django.conf.urls.static import static
from django.urls import path
from .views import client, voiture, employee, commande
from bdd.models.Client import Client
from bdd.models.Employee import Employee
from bdd.models.Voiture import Voiture
from bdd.models.Commande import Commande

urlpatterns = [

    #voiture
    path('', voiture.index, name="voitures"),
    path('voiture/<int:pk>/',
         login_required(DetailView.as_view(model=Voiture, template_name="vitrine/voiture_details.html")),
         name="voiture"),
    path('voitures/create', voiture.CreateVoiture.as_view(), name="create_voiture"),
    path('voitures/update/<int:pk>', voiture.UpdateVoiture.as_view(), name="update_voiture"),


    #client
    path('clients', client.client_list, name="clients"),
    path('clients/create', client.CreateClient.as_view(), name="create_client"),
    path('clients/update/<int:pk>', client.UpdateClient.as_view(), name="update_client"),
    path('client/<int:pk>',
          login_required(DetailView.as_view(model=Client, template_name="client/client_detail.html")),
         name="client_detail"),


    #employee
    path('employee', employee.employee_list, name="employees"),
    path('employee/create', employee.create_employee, name="create_employee"),
    path('employee/update/<int:pk>', employee.UpdateEmployee.as_view(), name="update_employee"),
    path('employee/<int:pk>',
          login_required(DetailView.as_view(model=Employee, template_name="employee/employee_details.html")),
         name="employee_details"),

    #commande
    path('commandes', commande.index, name="commandes"),
    path('commandes/create/<int:pk>', commande.CreateCommande.as_view(), name="create_commande"),
    path('commandes/<int:pk>',
          login_required(DetailView.as_view(model=Commande, template_name="commande/commande_detail.html")),
         name="commande_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

