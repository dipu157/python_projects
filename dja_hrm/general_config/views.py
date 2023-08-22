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
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addBankModal" data-bid="{bank.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-bid="{bank.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        

class save_bankData(View):
    def post(self, request):
        bid = request.POST.get('bid', '')
        form = BankCreateForm(request.POST or None, instance=None if bid == '' else Bank.objects.get(id=bid))
        if form.is_valid():
            bank = form.save(commit=False)
            bank.user = request.user
            bank.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        

class DeleteBank(View):
    def delete(self, request, bank_id):
        try:
            bank = Bank.objects.get(id=bank_id)
            bank.delete()
            return JsonResponse({"status": "success"})
        except Bank.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Bank does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
