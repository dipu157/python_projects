from django import forms
from .models import Bank, Working_Status, Duty_Location



class BankCreateForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name','branch_code','branch_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'branch_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'bcodeid'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'bnameid'}),
        }


class WStatusCreateForm(forms.ModelForm):
    class Meta:
        model = Working_Status
        fields = ['name','short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'snameid'}),
        }


class DLocationCreateForm(forms.ModelForm):
    class Meta:
        model = Duty_Location
        fields = ['location','description']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'locationid'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'descriptionid'}),
        }