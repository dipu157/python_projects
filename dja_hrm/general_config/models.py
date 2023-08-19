from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class Title(models.Model):
    name = models.CharField(max_length=240)
    description = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'titles'

    def __str__(self):
        return self.name
    
class Religions(models.Model):
    name = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'religions'

    def __str__(self):
        return self.name
    
class Banks(models.Model):
    name = models.CharField(max_length=40)
    branch_code = models.CharField(max_length=200, blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'banks'

    def __str__(self):
        return self.name

class Working_Status(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'working_status'

    def __str__(self):
        return self.name
    
class Bangladesh(models.Model):
    lang = models.CharField(max_length=2)
    division = models.CharField(max_length=20)
    district = models.CharField(max_length=25)
    thana = models.CharField(max_length=60)
    post_office = models.CharField(max_length=60)
    post_code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'bangladesh'

    def __str__(self):
        return self.district
    
class Duty_Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'duty_location'

    def __str__(self):
        return self.location