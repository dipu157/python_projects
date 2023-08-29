from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse

from company.models import Company
from .models import Designation
from .forms import DesignationCreateForm

class DesignationtHome(LoginRequiredMixin,View):
    def get(self, request):
        form = DesignationCreateForm()
        return render(request, "designation/designations.html", {'form': form})
    

class DesignationData(LoginRequiredMixin, View):
    def get(self, request):
        designations = Designation.objects.order_by('-created_at')
        data = []

        for counter, designation in enumerate(designations, start=1):
            data.append({
                'ID': counter,
                'Code': designation.designation_code,
                'Name': designation.name,
                'Short_name': designation.short_name,
                'Action': f'<a class="btn-edit" data-bs-toggle="modal" data-bs-target="#addDesignationModal" data-bid="{designation.id}"><i class="bx bxs-edit"></i></a>'
                          f'<a class="ms-3 btn-delete" data-bid="{designation.id}"><i class="bx bxs-trash"></i></a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})
        


class save_designationData(View):
    def post(self, request):
        desigid = request.POST.get('desigid', '')
        # print(bid)
        form = DesignationCreateForm(request.POST or None, instance=None if desigid == '' else Designation.objects.get(id=desigid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            designation = form.save(commit=False)
            designation.user = request.user
            designation.company = loggedInUserCompany
            designation.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'})