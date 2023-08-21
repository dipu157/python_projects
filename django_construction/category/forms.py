from django import forms
from .models import Category,SubCategory

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'desid', 'rows': 3, 'cols': 1}),
        }


class SubCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category','name', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'categoryid'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'desid', 'rows': 3, 'cols': 1}),
        }