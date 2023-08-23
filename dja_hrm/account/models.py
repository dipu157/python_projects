from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from company.models import Company

class Profile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)


    def __str__(self):
        return f'Profile of {self.user.username}'