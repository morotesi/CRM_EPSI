from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    selected="home"
    get_user = request.user.username
    return render(request, "vitrine/home.html", locals(), context={"user": get_user})