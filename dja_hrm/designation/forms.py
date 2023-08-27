from django import forms
from .models import Designation


class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name','short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'snameid'}),
        }