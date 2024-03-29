from django.db import models
from company.models import Company
from django.contrib.auth.models import User
from general_config.models import Title, Religion, Working_Status, Bank
from department.models import Department, Section
from designation.models import Designation

class EmpPersonal(models.Model):

    GENDER_CHOICES = (
        ('', 'Select One'),
        ('m', 'Male'),
        ('f', 'Female'),
    )

    BLOOD_GROUP_CHOICES = (
        ('', 'Select One'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
    )
    
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    title = models.ForeignKey(Title, on_delete=models.RESTRICT)
    religion = models.ForeignKey(Religion, on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    full_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='employee/',blank=True)
    signature = models.ImageField(upload_to='signature/',blank=True)
    email = models.EmailField(max_length=190, null=True, blank=True)
    pr_address = models.CharField(max_length=240, verbose_name="Present Address")
    pr_district = models.CharField(max_length=25, null=True, blank=True)
    pr_police_station = models.CharField(max_length=50, null=True, blank=True)
    pr_post_code = models.CharField(max_length=4, null=True, blank=True)
    pm_address = models.CharField(max_length=240, null=True, blank=True, verbose_name="Permanent Address")
    pm_district = models.CharField(max_length=25, null=True, blank=True)
    pm_police_station = models.CharField(max_length=50, null=True, blank=True)
    pm_post_code = models.CharField(max_length=4, null=True, blank=True)
    phone = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.CharField(max_length=150, null=True, blank=True)
    biography = models.CharField(max_length=150, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    spouse_name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=30, null=True, blank=True)
    last_education = models.CharField(max_length=240, null=True, blank=True)
    national_id = models.CharField(max_length=20, null=True, blank=True)
    is_printed = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'emp_personal'

    def __str__(self):
        return self.full_name
    

class EmpProfessional(models.Model):

    BOOL_CHOICES = (
        ('0', 'No'),
        ('1', 'Yes'),
    )

    CONFIRMPERIOD_CHOICES = (
        ('3', 'Three Month'),
        ('6', 'Six Month'),
        ('12', 'One Year'),
    )
    
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    emp_personal = models.ForeignKey(EmpPersonal, on_delete=models.RESTRICT)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    section = models.ForeignKey(Section, on_delete=models.RESTRICT)
    employee_id = models.PositiveIntegerField(unique=True)
    pf_no = models.PositiveIntegerField(default=0)
    designation = models.ForeignKey(Designation, on_delete=models.RESTRICT)
    report_to = models.PositiveIntegerField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    card_no = models.CharField(max_length=30, null=True, blank=True)
    card_printed = models.BooleanField(default=False)
    overtime = models.BooleanField(default=False, verbose_name="Overtime Eligibility")
    overtime_note = models.TextField(default="", null=True, blank=True, verbose_name="Overtime Instructions")
    transport = models.BooleanField(default=False, verbose_name="Transport Eligibility")
    transport_note = models.TextField(null=True, blank=True, verbose_name="Transport Instructions")
    pay_schale = models.PositiveIntegerField(default=0)
    pay_grade = models.CharField(max_length=50, null=True, blank=True)
    working_status = models.ForeignKey(Working_Status, on_delete=models.RESTRICT)
    confirm_probation = models.CharField(max_length=1, default='P')
    confirm_period = models.PositiveIntegerField(default=0)
    bank = models.ForeignKey(Bank, null=True, on_delete=models.RESTRICT)
    bank_acc_no = models.CharField(max_length=17, null=True, blank=True)
    status_change_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'emp_professional'

    def __str__(self):
        return self.emp_personal.full_name
  

class EmpEducation(models.Model):

    BOOL_CHOICES = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    emp_personal = models.ForeignKey(EmpPersonal, on_delete=models.RESTRICT)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, null=True, blank=True)
    institution = models.CharField(max_length=200)
    passing_year = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    degree_type = models.CharField(max_length=50)
    achive_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'emp_education'

    def __str__(self):
        return self.emp_education.name
