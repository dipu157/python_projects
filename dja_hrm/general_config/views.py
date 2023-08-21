from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Bank
from .forms import BankCreateForm


class BankHome(LoginRequiredMixin,View):
    def get(self, request):
        form = BankCreateForm()
        return render(request, "general_config/bank/banks.html", {'form': form})
