from django.urls import path
from .views import *



urlpatterns = [
    path('', ProductHome.as_view(), name='product'),
    path('productdata/', ProductData.as_view(), name='productdata'),
    path('createProduct/', save_productData.as_view(), name='createProduct'),
    path('delete_product/<int:product_id>/', DeleteProduct.as_view(), name='delete_product'),
    path('edit_product/<int:product_id>/', EditProduct.as_view(), name='edit_product'),
]