from django import forms
from .models import Contractor,Site

class ContractorCreateForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name','email','phone', 'address','nid','contractor_type','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phoneid'}),            
            'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'addressid', 'rows': 3, 'cols': 1}),
            'nid': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nid'}),
            'contractor_type': forms.TextInput(attrs={'class': 'form-control', 'id': 'ctid'}),
        }

class SiteCreateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['contractor','name','district','area', 'address','details','land_owner_name','owner_mobile',
                  'flat_qty','parking_qty','start_date','end_date','image']
        widgets = {
            'contractor': forms.Select(attrs={'class': 'form-control', 'id': 'contractorid'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'id': 'districtid'}),            
            'area': forms.TextInput(attrs={'class': 'form-control', 'id': 'areaid'}),            
            'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'addressid', 'rows': 3, 'cols': 1}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'id': 'detailsid', 'rows': 3, 'cols': 1}),
            'land_owner_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lonid'}),
            'owner_mobile': forms.TextInput(attrs={'class': 'form-control', 'id': 'omid'}),
            'flat_qty': forms.NumberInput(attrs={'class': 'form-control', 'id': 'fqid'}),
            'parking_qty': forms.NumberInput(attrs={'class': 'form-control', 'id': 'pqid'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'sdateid'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'endateid'}),
        }
        
class SiteEditForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['contractor','name','district','area', 'address','details','land_owner_name','owner_mobile',
                  'flat_qty','parking_qty','start_date','end_date','image']
        widgets = {
            'contractor': forms.Select(attrs={'class': 'form-control', 'id': 'ucontractorid'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'unameid'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'id': 'udistrictid'}),            
            'area': forms.TextInput(attrs={'class': 'form-control', 'id': 'uareaid'}),            
            'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'uaddressid', 'rows': 3, 'cols': 1}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'id': 'udetailsid', 'rows': 3, 'cols': 1}),
            'land_owner_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'ulonid'}),
            'owner_mobile': forms.TextInput(attrs={'class': 'form-control', 'id': 'uomid'}),
            'flat_qty': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ufqid'}),
            'parking_qty': forms.NumberInput(attrs={'class': 'form-control', 'id': 'upqid'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'usdateid'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'uendateid'}),
        }