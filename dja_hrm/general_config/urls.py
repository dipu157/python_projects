from django.urls import path
from .views import *



urlpatterns = [
    path('bank/', BankHome.as_view(), name='bank'),
    path('bank/bankdata/', BankData.as_view(), name='bankdata'),
    path('bank/createBank/', save_bankData.as_view(), name='createBank'),
    path('bank/delete_bank/<int:bank_id>/', DeleteBank.as_view(), name='delete_bank'),
    path('bank/edit_bank/<int:bank_id>/', EditBank.as_view(), name='edit_bank'),

    path('wstatus/', WStatusHome.as_view(), name='wstatus'),
    path('wstatus/wstatusdata/', WStatusData.as_view(), name='wstatusdata'),
    path('wstatus/createWStatus/', save_wstatusData.as_view(), name='createWStatus'),


    path('dlocation/', DLocationHome.as_view(), name='dlocation'),
    path('dlocation/dlocationdata/', DLocationData.as_view(), name='dlocationdata'),
]