from django.urls import path
from .views import *



urlpatterns = [
    path('', ContractorHome.as_view(), name='contractor'),
    path('contractordata/', ContractorData.as_view(), name='contractordata'),
    path('createContractor/', save_contractorData.as_view(), name='createContractor'),
    path('delete_contractor/<int:contractor_id>/', DeleteContractor.as_view(), name='delete_contractor'),
    path('edit_contractor/<int:supplier_id>/', EditContractor.as_view(), name='edit_contractor'),


    path('site/', SiteHome.as_view(), name='site'),
    path('site/sitedata/', SiteData.as_view(), name='sitedata'),
    path('createSite/', CreateSite.as_view(), name='createSite'),
    path('site/delete_site/<int:site_id>/', DeleteSite.as_view(), name='delete_site'),
    path('site/edit_site/<int:site_id>/', EditSite.as_view(), name='edit_site'),
    path('updateSite/', UpdateSite.as_view(), name='updateSite'),


    path('siteReportIndex/', SiteReportIndex.as_view(), name='siteReportIndex'),
    path('dateRangeSiteForm/', DateRangeSiteReport.as_view(), name='dateRangeSiteForm'),
]