from django.contrib import admin
from .models import Shift


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['name','short_name', 'from_time','to_time','duty_hour','status']
    search_fields = ['status', 'name','short_name']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'shifts'
        ordering = ['-created_at']
