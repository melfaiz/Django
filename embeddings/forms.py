from django import forms

class wordForm(forms.Form):
    word = forms.CharField(label='Word', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control', 'value' : 'mango'}))

class mathForm2(forms.Form):
    pos1 = forms.CharField(label='Positive embeddings', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control', 'value' : 'woman' }))
    pos2 = forms.CharField(label='Positive embeddings', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control', 'value' : 'king'}))
    neg = forms.CharField(label='Negative embeddings', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control', 'value' : 'man'}))
