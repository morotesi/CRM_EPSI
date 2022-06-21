from django.contrib import admin

# Register your models here.
from bdd.models.Voiture import Voiture
from bdd.models.Prix import Prix
from bdd.models.Client import Client
from bdd.models.Marque import Marque
from bdd.models.Employee import Employee
from bdd.models.Commande import Commande


admin.site.register(Marque)
admin.site.register(Prix)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Commande)



