from django.urls import path
from .views import *



urlpatterns = [
    path('', DepartmentHome.as_view(), name='department'),
    path('departmentdata/', DepartmentData.as_view(), name='departmentdata'),
]