from django import forms
from .models import Roster,DutyLocation
from shift.models import Shift



class RosterCreateForm(forms.ModelForm):
    class Meta:
        model = Roster
        fields = ['r_year','month_id','department', 'employee','day_01','day_02','day_03','day_04','day_05','day_06',
                  'day_07','day_08','day_09','day_10','day_11','day_12','day_13','day_14','day_15','day_16','day_17',
                  'day_18','day_19','day_20','day_21','day_22','day_23','day_24','day_25','day_26','day_27','day_28',
                  'day_29','day_30','day_31','loc_01','loc_02','loc_03','loc_04','status']