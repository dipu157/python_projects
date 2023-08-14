from django.urls import path
from .views import *


urlpatterns = [
    path('', BasicFormIndex.as_view(), name='basic_form'),
    path("bform/new/", BasicFormCreateView.as_view(), name="bform_add"),
]