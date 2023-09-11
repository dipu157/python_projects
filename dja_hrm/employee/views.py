from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse

from company.models import Company
from .models import EmpPersonal, EmpProfessional
from .forms import EmpPersonalCreateForm,EmpProfessionalCreateForm


class EmployeeHome(LoginRequiredMixin,View):
    def get(self, request):
        formPersonal = EmpPersonalCreateForm()
        formProfessional = EmpProfessionalCreateForm()
        return render(request, "employee/manage_employee.html", {'formPersonal': formPersonal, 'formProfessional': formProfessional})
    

class EmployeeData(LoginRequiredMixin, View):
    def get(self, request):
        employees = EmpProfessional.objects.order_by('-created_at')
        data = []

        for counter, employee in enumerate(employees, start=1):
            data.append({
                'ID': counter,
                'FullName': employee.emp_personal.full_name,
                'EmpId': employee.employee_id,
                'Department': employee.department.name,
                'Designation': employee.designation.name,
                'Joining_Date': employee.joining_date,
                'Working_Status': employee.working_status.name,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addDesignationModal" data-desigid="{employee.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-desigid="{employee.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
