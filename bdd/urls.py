from mspr import settings
from django.conf.urls.static import static
from django.urls import path
from bdd.views.voiture import index


urlpatterns = [
    path('', index, name="index"),
    path('voiture/<int:id>/', voiture_details, name="voiture")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)