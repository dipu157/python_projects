from django.db import models
from django.contrib.auth.models import User
from company.models import Company
from construction.models import Site
from supplier.models import Supplier
from product.models import Product

class Purchase(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    purchase_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    invoice_no = models.CharField(max_length=20,unique=True)
    purchase_date = models.DateField(null=True, blank=True)
    detail = models.CharField(max_length=50,null=True,blank=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_vat = models.DecimalField(max_digits=15, decimal_places=2, default=0,null=True)
    total_discount = models.DecimalField(max_digits=15, decimal_places=2, default=0,null=True)
    net_payable = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"purchase #{self.id}"
    
class PurchaseDetails(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    purchase = models.ForeignKey(Purchase, on_delete=models.RESTRICT)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    qty = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    vat = models.DecimalField(max_digits=15, decimal_places=2, default=0,null=True)
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0,null=True)
    net_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"purchase #{self.id}"