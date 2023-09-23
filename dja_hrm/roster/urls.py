from django.urls import path
from .views import *



urlpatterns = [
    path('', RosterEntryHome.as_view(), name='roster_entry'),
]