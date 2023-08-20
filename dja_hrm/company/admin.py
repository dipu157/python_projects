from django.contrib import admin
from .models import GroupCompany, Company


@admin.register(GroupCompany)
class GroupCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    list_filter = ['status', 'name']
    search_fields = ['name']
    
    class Meta:
        db_table = 'group_company'
        ordering = ['-created_at']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['group_company','name', 'address', 'phone']
    list_filter = ['group_company','status', 'name']
    search_fields = ['group_company','name']
    
    class Meta:
        db_table = 'company'
        ordering = ['-created_at']
