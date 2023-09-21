from django.urls import path
from .views import *



urlpatterns = [
    path('', EmployeeHome.as_view(), name='employee'),
    path('employeedata/', EmployeeData.as_view(), name='employeedata'),
    path('createEmpPersonal/', save_personalData.as_view(), name='createEmpPersonal'),
    path('createEmpProfessional/', save_professionalData.as_view(), name='createEmpProfessional'),
    path('delete_employee/<int:employee_id>/', DeleteEmployee.as_view(), name='delete_employee'),
    path('edit_employee/<int:employee_id>/', EditEmployee.as_view(), name='edit_employee'),
]