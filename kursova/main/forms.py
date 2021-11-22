from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('equation', 'data')
        widgets = {
            "data": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть значення а, b, c'
            })
            }