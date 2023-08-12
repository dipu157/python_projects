from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def frontDashboard(request):
    return render(request,'frontend/frontDashboard.html',{'section': 'frontDashboard'})