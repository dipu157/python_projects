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
    

class BankData(LoginRequiredMixin, View):
    def get(self, request):
        banks = Bank.objects.order_by('-created_at')
        data = []

        for counter, bank in enumerate(banks, start=1):
            data.append({
                'ID': counter,
                'Name': bank.name,
                'Branch_code': bank.branch_code,
                'Branch_name': bank.branch_name,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addBankModal" data-pid="{bank.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-pid="{bank.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
