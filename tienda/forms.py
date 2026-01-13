from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['nombre', 'email', 'telefono']

class CantidadForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, initial=1)
