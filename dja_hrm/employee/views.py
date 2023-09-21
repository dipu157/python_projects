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
                'Action': f'<a class="btn btn-sm btn-primary btn-edit" data-bs-toggle="modal" data-bs-target="#addEmployeeModal" data-empid="{employee.emp_personal_id}">Edit</a>'
                          f'<a class="ms-3 btn-danger btn btn-sm btn-delete" data-empid="{employee.emp_personal_id}">DEL</a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        
class save_personalData(View):
    def post(self, request):
        personid = request.POST.get('emp_personal', '')
        form = EmpPersonalCreateForm(request.POST or None, instance=None if personid == '' else EmpPersonal.objects.get(id=personid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            personal = form.save(commit=False)
            personal.user = request.user
            personal.company = loggedInUserCompany
            
            full_name_parts = [personal.first_name, personal.middle_name, personal.last_name]
            full_name = ' '.join(part for part in full_name_parts if part)
            personal.full_name = full_name
            
            personal.save()

            return JsonResponse({'status': 'save', 'id': personal.id})
        else:
            print(form.errors)
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error','errors': 'errors' , 'message': 'Form data is invalid'})
        
class save_professionalData(View):
    def post(self, request):
        professionid = request.POST.get('professionid', '')
        form = EmpProfessionalCreateForm(request.POST or None, instance=None if professionid == '' else EmpProfessional.objects.get(id=professionid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            professional = form.save(commit=False)
            professional.user = request.user
            professional.company = loggedInUserCompany
            
            professional.save()

            return JsonResponse({'status': 'save'})
        else:
            print(form.errors)
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error','errors': 'errors' ,'message': 'Form data is invalid'})


class DeleteEmployee(View):
    def delete(self, request, employee_id):
        try:
            employeeProfessional = EmpProfessional.objects.get(emp_personal_id=employee_id)
            employeePersonal = EmpPersonal.objects.get(id=employee_id)
            employeeProfessional.delete()
            employeePersonal.delete()
            return JsonResponse({"status": "success"})
        except employeePersonal.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Employee does not exist"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        

class EditEmployee(View):
    def get(self, request, employee_id):
        try:
            employee = EmpPersonal.objects.get(id=employee_id)
            data = {
                "id": employee.id,
                "title": employee.title.id,
                "religion": employee.religion.id,
                "first_name": employee.first_name,      
                "middle_name": employee.middle_name,      
                "last_name": employee.last_name,      
                "email": employee.email,      
                "phone": employee.phone,      
                "mobile": employee.mobile,      
                "father_name": employee.father_name,      
                "mother_name": employee.mother_name,      
                "spouse_name": employee.spouse_name, 
                "dob": employee.dob,
                "gender": employee.gender,
                "blood_group": employee.blood_group,
                "last_education": employee.last_education,
                "national_id": employee.national_id,
                "biography": employee.biography,
            }
            
            employeeProf = employeeProf.objects.get(emp_personal_id=employee_id)
            data1 = {
                "id": employeeProf.id,
                "department": employeeProf.department.id,
                "section": employeeProf.section.id,
                "employee_id": employeeProf.employee_id,      
                "designation": employeeProf.designation,      
                "joining_date": employeeProf.joining_date,      
                "card_no": employeeProf.card_no,      
                "overtime": employeeProf.overtime,      
                "transport": employeeProf.transport,      
                "working_status": employeeProf.working_status.id,      
                "confirm_period": employeeProf.confirm_period,
            }
            
            return JsonResponse(data)
        except EmpPersonal.DoesNotExist:
            return JsonResponse({"error": "Employee does not exist"})
        except Exception as e:
            return JsonResponse({"error": str(e)})