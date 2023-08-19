from django.contrib import admin
from .models import Designation

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['designation_code', 'name','short_name']
    search_fields = ['designation_code', 'name','short_name']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'designation'
        ordering = ['-created_at']
