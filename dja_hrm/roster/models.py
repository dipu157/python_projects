from django.db import models
from company.models import Company
from department.models import Department
from employee.models import EmpProfessional
from shift.models import Shift

from django.contrib.auth.models import User

class DutyLocation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'duty_locations'
        
    def __str__(self):
        return self.location
    

class Roster(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    r_year = models.PositiveIntegerField()
    month_id = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.RESTRICT, null=True, blank=True)
    employee = models.ForeignKey(EmpProfessional, on_delete=models.RESTRICT)
    day_01 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_01')
    day_02 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_02')
    day_03 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_03')
    day_04 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_04')
    day_05 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_05')
    day_06 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_06')
    day_07 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_07')
    loc_01 = models.ForeignKey(DutyLocation, on_delete=models.RESTRICT, null=True, blank=True, related_name='loc_01')
    day_08 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_08')
    day_09 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_09')
    day_10 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_10')
    day_11 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_11')
    day_12 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_12')
    day_13 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_13')
    day_14 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_14')
    loc_02 = models.ForeignKey(DutyLocation, on_delete=models.RESTRICT, null=True, blank=True, related_name='loc_02')
    day_15 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_15')
    day_16 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_16')
    day_17 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_17')
    day_18 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_18')
    day_19 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_19')
    day_20 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_20')
    day_21 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_21')
    loc_03 = models.ForeignKey(DutyLocation, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_03')
    day_22 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_22')
    day_23 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_23')
    day_24 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_24')
    day_25 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_25')
    day_26 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_26')
    day_27 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_27')
    day_28 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_28')
    loc_04 = models.ForeignKey(DutyLocation, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_04')
    day_29 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_29')
    day_30 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_30')
    day_31 = models.ForeignKey(Shift, on_delete=models.RESTRICT, null=True, blank=True, related_name='day_31')
    inserted_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='rosters_inserted_by')
    inserted_date = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='rosters_approved_by')
    approved_date = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='rosters_updated_by')
    updated_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'rosters'
        
