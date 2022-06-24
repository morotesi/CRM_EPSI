from django.contrib import admin
from bdd.models.Marque import Marque
from bdd.models.Employee import Employee
from bdd.models.Commande import Commande

# Register your models here.


admin.site.register(Marque)
admin.site.register(Employee)
admin.site.register(Commande)



