from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        
    path("backend/",include('authen.urls')),
    path("",include('frontend.urls')),
]
