from django.db import models
from company.models import Company
from django.contrib.auth.models import User

class Designation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    designation_code = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=25)
    description = models.CharField(max_length=240, null=True, blank=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'designations'
    
    def __str__(self):
        return self.name