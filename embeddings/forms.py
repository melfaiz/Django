from django import forms

class wordForm(forms.Form):
    word = forms.CharField(label='Word', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))

class mathForm(forms.Form):
    pos = forms.CharField(label='Positive embeddings', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    neg = forms.CharField(label='Negative embeddings', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
