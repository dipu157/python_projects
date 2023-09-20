from django import forms
from .models import EmpPersonal,EmpProfessional

class EmpPersonalCreateForm(forms.ModelForm):
    
    full_name = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = EmpPersonal
        fields = ['title', 'religion', 'first_name', 'middle_name', 'last_name', 'photo', 'signature', 'email', 
                  'phone','mobile','biography', 'father_name', 'mother_name', 'spouse_name', 'dob', 'gender', 'blood_group', 
                  'last_education', 'national_id']
        
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control', 'id': 'titleid'}),
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
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'biographyid'})
        }
        
        
class EmpProfessionalCreateForm(forms.ModelForm):
    class Meta:
        model = EmpProfessional
        fields = ['emp_personal', 'department', 'section', 'employee_id', 'pf_no', 'designation', 
                  'joining_date', 'card_no', 'overtime', 'transport', 'working_status', 'confirm_period']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'departmentid'}),
            'section': forms.Select(attrs={'class': 'form-control', 'id': 'sectionid'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'employeeid_id'}),
            'pf_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'pf_noid'}),
            'designation': forms.Select(attrs={'class': 'form-control', 'id': 'designationid'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'joining_dateid'}),
            'card_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'card_noid'}),
            'overtime': forms.Select(choices=EmpProfessional.BOOL_CHOICES, attrs={'class': 'form-control', 'id': 'overtimeid'}),
            'transport': forms.Select(choices=EmpProfessional.BOOL_CHOICES, attrs={'class': 'form-control', 'id': 'transportid'}),
            'working_status': forms.Select(attrs={'class': 'form-control', 'id': 'working_statusid'}),
            'bank': forms.Select(attrs={'class': 'form-control', 'id': 'bankid'}),
            'confirm_period': forms.Select(choices=EmpProfessional.CONFIRMPERIOD_CHOICES, attrs={'class': 'form-control', 'id': 'cperiodid'}),
        }
