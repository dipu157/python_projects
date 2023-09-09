from django.urls import path
from .views import *



urlpatterns = [
    path('', EmployeeHome.as_view(), name='employee'),
    path('employeedata/', EmployeeData.as_view(), name='employeedata'),
    # path('createDesignation/', save_designationData.as_view(), name='createDesignation'),
    # path('delete_designation/<int:designation_id>/', DeleteDesignation.as_view(), name='delete_designation'),
    # path('edit_designation/<int:designation_id>/', EditDesignation.as_view(), name='edit_designation'),
]