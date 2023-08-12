from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Supplier,Supplier_Ledger
from company.models import Company
from .forms import SupplierCreateForm


class SupplierHome(LoginRequiredMixin,View):
    def get(self, request):
        form = SupplierCreateForm()
        return render(request, "supplier/suppliers.html", {'form': form})

class SupplierData(LoginRequiredMixin, View):
    def get(self, request):
        suppliers = Supplier.objects.order_by('-created_at')
        data = []

        for counter, supplier in enumerate(suppliers, start=1):
            data.append({
                'ID': counter,
                'Name': supplier.name,
                'Email': supplier.email,
                'Phone': supplier.phone,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addSupplierModal" data-sid="{supplier.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-sid="{supplier.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})

class save_supplierData(View):
    def post(self, request):
        sid = request.POST.get('supid', '')  # retrieves the supid value from the POST data, or sets it to an empty string if not found.
        
        # creates an instance of the SupplierCreateForm form, passing the POST data and the instance argument. If sid is empty, 
        # it creates a new form for the create operation. If sid has a value, it retrieves the existing supplier object with that ID 
        # and passes it as the instance argument for the update operation.
        form = SupplierCreateForm(request.POST or None, instance=None if sid == '' else Supplier.objects.get(id=sid))
        if form.is_valid():
            supplier = form.save(commit=False) # saves the form data to the supplier object without committing to the database.
            supplier.company = get_object_or_404(Company, id=1)
            supplier.user = request.user
            supplier.save()

            if sid == '':

                supplier = Supplier.objects.get(id=supplier.id)
                # Create SupplierLedger entry only when sid is null
                Supplier_Ledger.objects.create(supplier=supplier, user=request.user)

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        

class DeleteSupplier(View):
    def delete(self, request, supplier_id):
        try:
            supplier = Supplier.objects.get(id=supplier_id)
            supplier.delete()
            return JsonResponse({"status": "success"})
        except Supplier.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Supplier does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        
class EditSupplier(View):
    def get(self, request, supplier_id):
        try:
            supplier = Supplier.objects.get(id=supplier_id)
            data = {
                "id": supplier.id,
                "name": supplier.name,
                "email": supplier.email,
                "phone": supplier.phone
            }
            return JsonResponse(data)
        except Supplier.DoesNotExist:
            return JsonResponse({"error": "Supplier does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        


class SupplierLedger(LoginRequiredMixin,View):
    def get(self, request):        
        supplier_ledger = Supplier_Ledger.objects.order_by('-created_at')

        return render(request, "supplier/supplier_ledger.html",{'supplier_ledger':supplier_ledger})