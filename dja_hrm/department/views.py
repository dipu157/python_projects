from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse

from company.models import Company
from .models import Department, Section
from .forms import DepartmentCreateForm

class DepartmentHome(LoginRequiredMixin,View):
    def get(self, request):
        form = DepartmentCreateForm()
        return render(request, "department/departments.html", {'form': form})
    

class DepartmentData(LoginRequiredMixin, View):
    def get(self, request):
        departments = Department.objects.order_by('-created_at')
        data = []

        for counter, department in enumerate(departments, start=1):
            data.append({
                'ID': counter,
                'Code': department.department_code,
                'Name': department.name,
                'Short_name': department.short_name,
                'Report_to': department.report_to,
                'Headed_By': department.headed_by,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addBankModal" data-bid="{department.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-bid="{department.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        


class save_departmentData(View):
    def post(self, request):
        deptid = request.POST.get('departmentid', '')
        #print(deptid)
        form = DepartmentCreateForm(request.POST or None, instance=None if deptid == '' else Department.objects.get(id=deptid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            department = form.save(commit=False)
            department.user = request.user
            department.company = loggedInUserCompany
            department.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})
        
class DeleteDepartment(View):
    def delete(self, request, department_id):
        try:
            department = Department.objects.get(id=department_id)
            department.delete()
            return JsonResponse({"status": "success"})
        except Department.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Department does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        
        
class EditDepartment(View):
    def get(self, request, department_id):
        try:
            department = Department.objects.get(id=department_id)
            data = {
                "id": department.id,
                "code": department.department_code,
                "name": department.name,      
                "short_name": department.short_name
            }
            return JsonResponse(data)
        except Department.DoesNotExist:
            return JsonResponse({"error": "Department does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})