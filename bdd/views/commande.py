from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def add_to_card(request, pk):
    customer = request.user
    voiture = get_object_or_404(Voiture, pk=pk)