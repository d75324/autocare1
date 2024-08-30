from django import forms
from django.contrib.auth.models import User, Group
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        # Filtra los usuarios que pertenecen al grupo "Mecánicos" a través del perfil
        self.fields['car_mechanic'].queryset = User.objects.filter(groups__name='Mecanicos')
