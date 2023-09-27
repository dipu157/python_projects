from django import forms
from .models import Shift

class ShiftCreateForm(forms.ModelForm):
 
    class Meta:
        model = Shift
        fields = ['name', 'short_name', 'from_time', 'to_time', 'duty_hour', 'end_next_day', 
                  'effective_date','description']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'short_nameid'}),
            'from_time': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'from_timeid'}),
            'to_time': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'to_timeid'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'short_nameid'}),
            'end_next_day': forms.TextInput(attrs={'class': 'form-control', 'id': 'endid'}),    
            'effective_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'edateid'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'descriptionid'})
        }