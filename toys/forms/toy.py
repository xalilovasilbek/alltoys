from django import forms
from toys.models import Toy


class ToyForm(forms.Form):
    name = forms.CharField(label='Toy name', required=True)
    description = forms.CharField(required=False)


class ToyModelForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['name', 'description', 'price']
