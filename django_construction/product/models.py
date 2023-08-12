from django.db import models
from django.contrib.auth.models import User
from supplier.models import Supplier
from category.models import SubCategory

class Product(models.Model):
    name = models.CharField(max_length=240)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.RESTRICT)
    details = models.CharField(max_length=150, null=True, blank=True)
    in_stock = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
