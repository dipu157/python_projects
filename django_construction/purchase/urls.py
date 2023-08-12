from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseHome.as_view(), name='purchase'),
    path('productBySupplier/', ProductBySupplierId.as_view(), name='productBySupplier'),
    path('purchaseSave/', SavePurchaseData.as_view(), name='purchaseSave'),
    path('purchaseList/', purchaseListData.as_view(), name='purchaseList'),
]