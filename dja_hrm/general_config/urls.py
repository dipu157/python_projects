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
    path('wstatus/delete_wstatus/<int:wstatus_id>/', DeleteWStatus.as_view(), name='delete_wstatus'),
    path('wstatus/edit_wstatus/<int:wstatus_id>/', EditWStatus.as_view(), name='edit_wstatus'),


    path('dlocation/', DLocationHome.as_view(), name='dlocation'),
    path('dlocation/dlocationdata/', DLocationData.as_view(), name='dlocationdata'),
    path('dlocation/createDLocation/', save_dlocationData.as_view(), name='createDLocation'),
    path('dlocation/delete_dlocation/<int:dlocation_id>/', DeleteDLocation.as_view(), name='delete_dlocation'),
]