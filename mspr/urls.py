"""mspr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from mspr import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from bdd.views.voiture import index
from django.views.defaults import server_error


urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    #path('voiture/<int:id>/', voiture_details, name="voiture")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
