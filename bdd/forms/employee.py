from django import forms
from bdd.models.Employee import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    last_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class UserEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('no_tel', 'rue', 'ville', 'code_postale')