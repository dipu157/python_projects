from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=240)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
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

    def __str__(self):
        return self.name
