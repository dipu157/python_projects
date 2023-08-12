from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class Supplier(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    name = models.CharField(max_length=240)
    email = models.EmailField(max_length=190, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Supplier_Ledger(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    paid = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    due = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.supplier)
    
    
class SupplierAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    purchase = models.ForeignKey('purchase.Purchase', on_delete=models.RESTRICT)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    due = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Supplier Account #{self.id}"
    
class SupplierPayment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    purchase = models.ForeignKey('purchase.Purchase', on_delete=models.RESTRICT)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    payment_type = models.CharField(max_length=100, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_phone = models.CharField(max_length=20, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Supplier Payment #{self.id}"