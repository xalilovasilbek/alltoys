from django import forms
from toys.models import Employee


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
