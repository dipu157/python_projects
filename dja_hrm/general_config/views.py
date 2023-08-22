from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Bank, Working_Status, Duty_Location
from .forms import BankCreateForm, WStatusCreateForm, DLocationCreateForm


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
        bid = request.POST.get('bankid', '')
        # print(bid)
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


class EditBank(View):
    def get(self, request, bank_id):
        try:
            bank = Bank.objects.get(id=bank_id)
            data = {
                "id": bank.id,
                "name": bank.name,
                "branch_code": bank.branch_code,
                "branch_name": bank.branch_name
            }
            return JsonResponse(data)
        except Bank.DoesNotExist:
            return JsonResponse({"error": "Bank does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        

class WStatusHome(LoginRequiredMixin,View):
    def get(self, request):
        form = WStatusCreateForm()
        return render(request, "general_config/working_status/wstatus.html", {'form': form})    


class WStatusData(LoginRequiredMixin, View):
    def get(self, request):
        wstatuses = Working_Status.objects.order_by('-created_at')
        data = []

        for counter, wstatus in enumerate(wstatuses, start=1):
            data.append({
                'ID': counter,
                'Name': wstatus.name,
                'Short_name': wstatus.short_name,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addWStatusModal" data-wsid="{wstatus.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-wsid="{wstatus.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        


class DLocationHome(LoginRequiredMixin,View):
    def get(self, request):
        form = DLocationCreateForm()
        return render(request, "general_config/duty_location/dlocations.html", {'form': form})
    

class DLocationData(LoginRequiredMixin, View):
    def get(self, request):
        dlocations = Duty_Location.objects.order_by('-created_at')
        print(dlocations)
        data = []

        for counter, dlocation in enumerate(dlocations, start=1):
            data.append({
                'ID': counter,
                'Location': dlocation.location,
                'Description': dlocation.description,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addWStatusModal" data-wsid="{dlocation.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-wsid="{dlocation.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})