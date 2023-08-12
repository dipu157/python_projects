from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'country', 'phone', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'address']
    
    class Meta:
        db_table = 'company'
        ordering = ['-created_at']
