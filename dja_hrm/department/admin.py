from django.contrib import admin
from .models import Department,Section


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_code', 'name','short_name', 'headed_by','roster_year','roster_month_id']
    search_fields = ['department_code', 'name','short_name']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'department'
        ordering = ['-created_at']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['department','section_code', 'name','short_name', 'headed_by']
    search_fields = ['department', 'name','short_name']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'section'
        ordering = ['-created_at']