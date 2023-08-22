from django.urls import path
from .views import *



urlpatterns = [
    path('bank/', BankHome.as_view(), name='bank'),
    path('bank/bankdata/', BankData.as_view(), name='bankdata'),
]