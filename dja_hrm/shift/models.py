from django.db import models
from company.models import Company
from django.contrib.auth.models import User
from django.utils import timezone

class Shift(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    from_time = models.TimeField(default='00:00')
    to_time = models.TimeField(default='00:00')
    duty_hour = models.SmallIntegerField(default=0)
    end_next_day = models.BooleanField(default=False)
    effective_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    terminal = models.GenericIPAddressField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'shifts'
        
    def __str__(self):
        return self.name
