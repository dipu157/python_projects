from django import forms
from .models import Department, Section


class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_code','name','short_name']
        widgets = {
            'department_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'codeid'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'snameid'}),
        }


class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['department','section_code','name','short_name']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'departmentid'}),
            'section_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'codeid'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'snameid'}),
        }