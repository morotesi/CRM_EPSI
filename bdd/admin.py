from django.contrib import admin
# Register your models here.
from bdd.models import Voiture,Marque,Prix,Client,Role,Employee,EmployeeAdmin,Commande,ClientAdmin,RoleAdmin,CommandeAdmin

admin.site.register(Voiture)
admin.site.register(Marque)
admin.site.register(Prix)
admin.site.register(Client, ClientAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Commande,CommandeAdmin)



