from django import forms
from .models import Designation


class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['designation_code','name','short_name']
        widgets = {
            'designation_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'codeid'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'snameid'}),
        }