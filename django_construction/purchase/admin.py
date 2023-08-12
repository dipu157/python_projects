from django.contrib import admin
from .models import Purchase,PurchaseDetails


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['purchase_code','supplier','site', 'invoice_no', 'purchase_date','net_payable']
    list_filter = ['supplier', 'site']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'purchase'
        ordering = ['-created_at']
        
@admin.register(PurchaseDetails)
class PurchaseDetailsAdmin(admin.ModelAdmin):
    list_display = ['purchase','supplier','site','product', 'qty', 'price','net_amount']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'purchase_details'
        ordering = ['-created_at']