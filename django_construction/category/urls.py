from django.urls import path
from . import views



urlpatterns = [
    path('', views.CategoryHome, name='category'),
    path('saveCategory/', views.save_categoryData, name='saveCategory'),
    path('deleteCategory/', views.delete_categoryData, name='deleteCategory'),
    path('editCategory/', views.edit_categoryData, name='editCategory'),

    path('subcategory/', views.SubCategoryHome, name='subcategory'),
    path('saveSubCategory/', views.save_subcategoryData, name='saveSubCategory'),
    path('deleteSubCategory/', views.delete_subcategoryData, name='deleteSubCategory'),
    path('editSubCategory/', views.edit_subcategoryData, name='editSubCategory'),
]