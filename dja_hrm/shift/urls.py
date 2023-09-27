from django.urls import path
from .views import *



urlpatterns = [
    path('', ShiftHome.as_view(), name='shift'),
    path('shiftdata/', ShiftData.as_view(), name='shiftdata'),
    path('createShift/', save_shiftData.as_view(), name='createShift'),
    path('delete_shift/<int:shift_id>/', DeleteShift.as_view(), name='delete_shift'),
    path('edit_shift/<int:shift_id>/', EditShift.as_view(), name='edit_shift'),
]