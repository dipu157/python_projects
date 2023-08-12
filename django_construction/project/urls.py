from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('authen.urls')),
    path("category/",include('category.urls')),
    path("supplier/",include('supplier.urls')),
    path("product/",include('product.urls')),
    path("contractor/",include('construction.urls')),
    path("purchase/",include('purchase.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)