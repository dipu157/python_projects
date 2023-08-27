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
        

