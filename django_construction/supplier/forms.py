from django import forms
from .models import Supplier

class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','email','phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phoneid'}),
        }