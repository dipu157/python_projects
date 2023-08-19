from django.db import models
from company.models import Company
from django.contrib.auth.models import User
import datetime

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    department_code = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=25)
    description = models.CharField(max_length=240, null=True, blank=True)
    started_from = models.DateField(default=datetime.date.today)
    report_to = models.PositiveIntegerField(null=True, blank=True)
    approval_authority = models.PositiveIntegerField(null=True, blank=True)
    headed_by = models.PositiveIntegerField(null=True, blank=True)
    second_man = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=190, null=True, blank=True, unique=True)
    status = models.BooleanField(default=True)
    emp_count = models.PositiveIntegerField(default=0)
    approved_manpower = models.PositiveIntegerField(default=0)
    top_rank = models.CharField(max_length=100, null=True, blank=True)
    roster_year = models.PositiveIntegerField(default=2023)
    roster_month_id = models.PositiveIntegerField(default=0)
    leave_steps = models.CharField(max_length=4, default='1111')
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'departments'
        

class Section(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    section_code = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=25)
    description = models.CharField(max_length=240, null=True, blank=True)
    started_from = models.DateField(auto_now_add=True)
    report_to = models.PositiveIntegerField(null=True, blank=True)
    approval_authority = models.PositiveIntegerField(null=True, blank=True)
    headed_by = models.PositiveIntegerField(null=True, blank=True)
    second_man = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=190, null=True, blank=True, unique=True)
    status = models.BooleanField(default=True)
    emp_count = models.PositiveIntegerField(default=0)
    approved_manpower = models.PositiveIntegerField(default=0)
    top_rank = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sections'
