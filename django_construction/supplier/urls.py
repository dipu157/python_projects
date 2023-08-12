from django.urls import path
from .views import *



urlpatterns = [
    path('', SupplierHome.as_view(), name='supplier'),
    path('supplierdata/', SupplierData.as_view(), name='supplierdata'),
    path('createSupplier/', save_supplierData.as_view(), name='createSupplier'),
    path('delete_supplier/<int:supplier_id>/', DeleteSupplier.as_view(), name='delete_supplier'),
    path('edit_supplier/<int:supplier_id>/', EditSupplier.as_view(), name='edit_supplier'),


    path('supplierLedger/', SupplierLedger.as_view(), name='supplierLedger'),
]