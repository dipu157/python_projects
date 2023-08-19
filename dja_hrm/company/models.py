from django.db import models
from django.contrib.auth.models import User


class GroupCompany(models.Model):
    name = models.CharField(max_length=240)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, null=True, blank=True)
    post_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=190, unique=True, null=True, blank=True)
    website = models.URLField(max_length=190, null=True, blank=True)
    currency = models.CharField(max_length=3, default='BDT')
    locale = models.CharField(max_length=20, default='en-US', help_text='English, Bangla')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'group_company'
        
    def __str__(self):
        return self.name
    
class Company(models.Model):
    group_company = models.ForeignKey(GroupCompany, on_delete=models.RESTRICT)
    name = models.CharField(max_length=240)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    post_code = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=190, unique=True, blank=True, null=True)
    website = models.CharField(max_length=190, blank=True, null=True)
    logo_img = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=3, default='BDT')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name
