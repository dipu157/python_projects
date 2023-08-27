from django.urls import path
from .views import *



urlpatterns = [
    path('', DesignationtHome.as_view(), name='designation'),
    path('designationdata/', DesignationData.as_view(), name='designationdata'),
]