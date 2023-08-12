from django.contrib import admin
from .models import BasicForm


@admin.register(BasicForm)
class BasicFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','blood_group','description', 'image']
    list_filter = ['status', 'name', 'blood_group']
    search_fields = ['name','code']
    exclude = ['user'] 

    def save_model(self, request, obj, form, change):
        obj.user = request.user  # Assign the logged-in user
        obj.save()
    
    class Meta:
        db_table = 'base_form'
        ordering = ['-created_at']
