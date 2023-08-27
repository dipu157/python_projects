from django import forms
from .models import Department, Section


class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'snameid'}),
        }