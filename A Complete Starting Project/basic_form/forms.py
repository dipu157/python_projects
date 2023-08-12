from django import forms
from .models import BasicForm

class BaseFormCreateForm(forms.ModelForm):
    BLOOD_GROUP_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]

    class Meta:
        model = BasicForm
        fields = ['name','blood_group','slug','description','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'desid', 'rows': 3, 'cols': 1}),
            # 'status': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'statusid'}),
        }
    
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))