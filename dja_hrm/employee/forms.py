from django import forms
from .models import EmpPersonal

class EmpPersonalCreateForm(forms.ModelForm):
    class Meta:
        model = EmpPersonal
        fields = ['title', 'religion', 'first_name', 'middle_name', 'last_name', 'photo', 'signature', 'email', 
                  'phone', 'father_name', 'mother_name', 'spouse_name', 'dob', 'gender', 'blood_group', 
                  'last_education', 'national_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'titleid'}),
            'religion': forms.Select(attrs={'class': 'form-control', 'id': 'religionid'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_nameid'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'middle_nameid'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phoneid'}),   
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'father_nameid'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'mother_nameid'}),
            'spouse_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'spouse_nameid'}), 
            'dob': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'dobid'}),
            'gender': forms.Select(choices=EmpPersonal.GENDER_CHOICES, attrs={'class': 'form-control', 'id': 'genderid'}),
            'blood_group': forms.Select(choices=EmpPersonal.BLOOD_GROUP_CHOICES, attrs={'class': 'form-control', 'id': 'blood_groupid'}),
            'last_education': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_educationid'}),    
            'national_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'nationalidid'}),
        }
