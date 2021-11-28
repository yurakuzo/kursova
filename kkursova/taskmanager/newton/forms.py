from .models import Newtons
from django.forms import ModelForm, NumberInput, TextInput


class NewtonsForm(ModelForm):
    class Meta:
        model = Newtons
        fields = ('f', 'x0', 'max_iter', 'eps')
        widgets = {
            'f': 
                TextInput(attrs={'class': 'form-control',
                                 'placeholder': 'Введіть функцію'}),
            'x0': 
                NumberInput(attrs={'class': 'form-control',
                                 'placeholder': 'x0'}),
            'max_iter': 
                NumberInput(attrs={'class': 'form-control',
                                 'placeholder': 'N'}),
            'eps': 
                NumberInput(attrs={'class': 'form-control',
                                 'placeholder': 'eps'}),
        }