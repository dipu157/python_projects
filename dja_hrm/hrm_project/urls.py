from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('account.urls')),
    path("gconfig/",include('general_config.urls')),
    path("department/",include('department.urls')),
    path("designation/",include('designation.urls')),
    path("employee/",include('employee.urls')),
    path("roster_entry/",include('roster.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)