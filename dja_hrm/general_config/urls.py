from django.urls import path
from .views import *



urlpatterns = [
    path('bank/', BankHome.as_view(), name='bank'),
    path('bank/bankdata/', BankData.as_view(), name='bankdata'),
    path('bank/createBank/', save_bankData.as_view(), name='createBank'),
    path('bank/delete_bank/<int:bank_id>/', DeleteBank.as_view(), name='delete_bank'),
]