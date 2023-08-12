from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class Contractor(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    name = models.CharField(max_length=240)
    email = models.EmailField(max_length=190, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nid = models.CharField(max_length=50, blank=True, null=True)
    contractor_type = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='contractor/',blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class Site(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    name = models.CharField(max_length=240)
    district = models.CharField(max_length=240,default="Dhaka")
    area = models.CharField(max_length=240)
    address = models.CharField(max_length=200, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    land_owner_name = models.CharField(max_length=240)
    owner_mobile = models.CharField(max_length=200, blank=True, null=True)
    flat_qty = models.CharField(max_length=20)
    parking_qty = models.CharField(max_length=20)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='site/',blank=True)
    status = models.BooleanField(default=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
