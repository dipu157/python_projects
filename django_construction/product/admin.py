from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'sub_category','in_stock']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'product'
        ordering = ['-created_at']
