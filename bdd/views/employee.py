from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.db import models, transaction
from bdd.models.Employee import Employee
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bdd.forms.employee import UserEmployeeForm
from django.views.generic import UpdateView

from bdd.forms.employee import ExtendedUserCreationForm

@login_required
def create_employee(request):
    if request.method=='POST':
        form = ExtendedUserCreationForm(request.POST)
        employee_form = UserEmployeeForm(request.POST)

        if form.is_valid() and employee_form.is_valid:
            user = form.save()

            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()

            return redirect('employees')

        else:
            form = ExtendedUserCreationForm()
            employee_form = UserEmployeeForm()
            context = {'user_form': form , 'employee_form': employee_form}

        return render(request, 'employees/employee_list.html', context)


@login_required
def employee_list(request):
    selected="employees"
    employee_list= User.objects.all().select_related('employee')

    #pagination pour nbre d'elements par page
    paginator = Paginator(employee_list.order_by('date_joined'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        employee_list = paginator.page(page)
    except EmptyPage:
        client_list = paginator.page(paginator.num_pages())
    return render(request, "employee/employee_list.html", locals())


@login_required
@transaction.atomic
def update_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        employee_form = EmployeeForm(request.POST, instance=request.user.employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('settings:employee')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        employee_form = EmployeeForm(instance=request.user.employee)
    return render(request, 'employee/employee_details.html',)

class UpdateEmployee(UpdateView, LoginRequiredMixin):
    model = Employee
    form_class = UserEmployeeForm
    template_name = "employee/employee_form.html"

    def get_success_url(self):
        return reverse_lazy("employee_details", kwargs={"pk": self.object.id})