from django.urls import path
from .views import *



urlpatterns = [
    path('', DepartmentHome.as_view(), name='department'),
    path('departmentdata/', DepartmentData.as_view(), name='departmentdata'),
    path('createDepartment/', save_departmentData.as_view(), name='createDepartment'),
    path('delete_department/<int:department_id>/', DeleteDepartment.as_view(), name='delete_department'),
    path('edit_department/<int:department_id>/', EditDepartment.as_view(), name='edit_department'),

    path('section/', SectionHome.as_view(), name='section'),
    path('section/sectiondata/', SectionData.as_view(), name='sectiondata'),
    path('section/createSection/', save_sectionData.as_view(), name='createSection'),
    path('section/edit_section/<int:section_id>/', EditSection.as_view(), name='edit_section'),
]