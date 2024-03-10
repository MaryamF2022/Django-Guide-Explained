from django import forms
from .models import Books

class AddForm(forms.ModelForm):

    class Meta:
        model=Books
        fields =('title', 'author', 'genre', 'isbn')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }