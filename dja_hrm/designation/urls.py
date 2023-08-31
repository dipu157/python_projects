from django.urls import path
from .views import *



urlpatterns = [
    path('', DesignationtHome.as_view(), name='designation'),
    path('designationdata/', DesignationData.as_view(), name='designationdata'),
    path('createDesignation/', save_designationData.as_view(), name='createDesignation'),
    path('delete_designation/<int:designation_id>/', DeleteDesignation.as_view(), name='delete_designation'),
    path('edit_designation/<int:designation_id>/', EditDesignation.as_view(), name='edit_designation'),
]