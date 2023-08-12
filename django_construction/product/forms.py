from django import forms
from .models import Product



class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','supplier','sub_category', 'details','unit_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplierid'}),
            'sub_category': forms.Select(attrs={'class': 'form-control', 'id': 'scatid'}),            
            'details': forms.Textarea(attrs={'class': 'form-control', 'id': 'detailsid', 'rows': 3, 'cols': 1}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'upid'}),
        }