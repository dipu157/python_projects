from django.contrib import admin
from .models import Contractor,Site


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['contractor_type', 'name','email', 'phone','nid','image']
    search_fields = ['name']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'contractor'
        ordering = ['-created_at']


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'area','land_owner_name', 'flat_qty','parking_qty','contractor','image']
    search_fields = ['name','area','contractor']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'site'
        ordering = ['-created_at']