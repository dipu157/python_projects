from django.urls import path
from .views import *



urlpatterns = [
    path('', DepartmentHome.as_view(), name='department'),
    path('departmentdata/', DepartmentData.as_view(), name='departmentdata'),
    path('createDepartment/', save_departmentData.as_view(), name='createDepartment'),
    path('delete_department/<int:department_id>/', DeleteDepartment.as_view(), name='delete_department'),
    path('edit_department/<int:department_id>/', EditDepartment.as_view(), name='edit_department'),
]