from django import forms
from .models import Point

class ChartForm(forms.ModelForm):

    class Meta:
       model = Point
       fields=['x']
       widgets = {
           'x': forms.NumberInput(attrs={ 'type':'number' , 'step' : '0.01', 'min': '0', 'class': 'form-control', 'id': 'inputField', 'placeholder':'Enter the point value'}),
    }

