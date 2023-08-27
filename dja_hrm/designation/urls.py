from django.urls import path
from .views import *



urlpatterns = [
    path('', DesignationtHome.as_view(), name='department'),
    path('designationdata/', DesignationData.as_view(), name='designationdata'),
]