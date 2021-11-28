from .models import Quadratics
from django.forms import ModelForm, NumberInput


class QuadraticsForm(ModelForm):
    class Meta:
        model = Quadratics
        fields = ('a', 'b', 'c')
        widgets = {
            'a': 
                NumberInput(attrs={'class': 'form-control',
                                 'placeholder': 'Введіть коефіцієнт а'}),
            'b': 
                NumberInput(attrs={'class': 'form-control',
                                 'placeholder': 'Введіть коефіцієнт b'}),
            'c': 
                NumberInput(attrs={'class': 'form-control',
                                 'placeholder': 'Введіть коефіцієнт c'})
        }