from django import forms
from .models import Bank



class BankCreateForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name','branch_code','branch_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'branch_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'bcodeid'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'bnameid'}),
        }