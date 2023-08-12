from django.contrib import admin
from .models import Supplier,Supplier_Ledger,SupplierAccount,SupplierPayment


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_filter = ['name', 'phone']
    search_fields = ['name']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'supplier'
        ordering = ['-created_at']

@admin.register(Supplier_Ledger)
class SupplierLedgerAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'total_amount', 'paid','due']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'supplier_ledger'
        ordering = ['-created_at']
        
        
@admin.register(SupplierAccount)
class SupplierAccountAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'total_amount', 'paid_amount','due']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'supplier_account'
        ordering = ['-created_at']
        
        
        
@admin.register(SupplierPayment)
class SupplierPaymentAdmin(admin.ModelAdmin):
    list_display = ['supplier','receiver_name', 'paid_amount']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'supplier_payment'
        ordering = ['-created_at']
