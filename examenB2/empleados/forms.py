from django import forms
from .models import Empleado

class AgregarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado

        fields = ['nombre',
                  'apat',
                  'amat',
                  'fechanacimiento',
                  'correo','genero',
                  'telefono',
                  'celular',
                  'fechaingreso',
                  'empresa',
                  'departamento'
                ]

    def __init__(self, *args, **kwargs):
        super(AgregarEmpleado, self).__init__(*args, **kwargs)
        self.fields['genero'].required = False
        self.fields['telefono'].required = False
        self.fields['celular'].required = False
        self.fields['fechanacimiento'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        self.fields['fechaingreso'].widget.attrs['placeholder'] = 'yyyy-mm-dd'