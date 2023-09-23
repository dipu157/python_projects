from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse

from company.models import Company
from .models import EmpPersonal, EmpProfessional
from .forms import RosterCreateForm


class RosterEntryHome(LoginRequiredMixin,View):
    def get(self, request):
        rosterCreate = RosterCreateForm()
        return render(request, "roster/create_roster.html", {'rosterCreate': rosterCreate})
    
