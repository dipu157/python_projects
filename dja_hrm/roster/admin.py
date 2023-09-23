from django.contrib import admin
from .models import DutyLocation, Roster


@admin.register(DutyLocation)
class DutyLocationAdmin(admin.ModelAdmin):
    list_display = ['location','description', 'status']
    search_fields = ['status', 'location','description']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'duty_locations'
        ordering = ['-created_at']
        
@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = ['employee','r_year', 'month_id', 'department']
    search_fields = ['employee', 'r_year','month_id','department']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'rosters'
        ordering = ['-created_at']
