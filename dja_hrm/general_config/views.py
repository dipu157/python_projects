from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Bank, Working_Status, Duty_Location
from company.models import Company
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
        


class save_wstatusData(View):
    def post(self, request):
        wsid = request.POST.get('wstatusid', '')
        form = WStatusCreateForm(request.POST or None, instance=None if wsid == '' else Working_Status.objects.get(id=wsid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            wstatus = form.save(commit=False)
            wstatus.user = request.user            
            wstatus.company = loggedInUserCompany
            wstatus.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        

class DeleteWStatus(View):
    def delete(self, request, wstatus_id):
        try:
            wstatus = Working_Status.objects.get(id=wstatus_id)
            wstatus.delete()
            return JsonResponse({"status": "success"})
        except Working_Status.DoesNotExist:
            return JsonResponse({"status": "error", "message": "wstatus does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        
class EditWStatus(View):
    def get(self, request, wstatus_id):
        try:
            wstatus = Working_Status.objects.get(id=wstatus_id)
            data = {
                "id": wstatus.id,
                "name": wstatus.name,
                "short_name": wstatus.short_name
            }
            return JsonResponse(data)
        except Working_Status.DoesNotExist:
            return JsonResponse({"error": "wstatus does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        
               
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
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addDLocationModal" data-dlid="{dlocation.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-dlid="{dlocation.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        


class save_dlocationData(View):
    def post(self, request):
        dlocid = request.POST.get('dlocationid', '')
        form = DLocationCreateForm(request.POST or None, instance=None if dlocid == '' else Duty_Location.objects.get(id=dlocid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            dlocation = form.save(commit=False)
            dlocation.user = request.user            
            dlocation.company = loggedInUserCompany
            dlocation.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        

class DeleteDLocation(View):
    def delete(self, request, dlocation_id):
        try:
            dlocation = Duty_Location.objects.get(id=dlocation_id)
            dlocation.delete()
            return JsonResponse({"status": "success"})
        except Duty_Location.DoesNotExist:
            return JsonResponse({"status": "error", "message": "dlocation does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        

class EditDLocation(View):
    def get(self, request, dlocation_id):
        try:
            dlocation = Duty_Location.objects.get(id=dlocation_id)
            data = {
                "id": dlocation.id,
                "location": dlocation.location,
                "description": dlocation.description
            }
            return JsonResponse(data)
        except Duty_Location.DoesNotExist:
            return JsonResponse({"error": "dlocation does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})