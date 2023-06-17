from django import forms
from .models import *

class SupervisionForm(forms.ModelForm):
    class Meta:
        model = Supervision
        fields = '__all__'
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = '__all__'