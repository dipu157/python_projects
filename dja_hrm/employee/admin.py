from django.contrib import admin
from .models import EmpPersonal, EmpProfessional

@admin.register(EmpPersonal)
class EmpPersonalAdmin(admin.ModelAdmin):
    list_display = ['title','photo','full_name', 'email','mobile', 'religion','dob','blood_group']
    search_fields = ['full_name', 'religion','blood_group']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'emp_personal'
        ordering = ['-created_at']


@admin.register(EmpProfessional)
class EmpProfessionalAdmin(admin.ModelAdmin):
    list_display = ['emp_personal','department', 'employee_id','pf_no', 'designation','joining_date','working_status_id']
    search_fields = ['department', 'designation','working_status_id']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'emp_professional'
        ordering = ['-created_at']
