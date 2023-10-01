from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse

from company.models import Company
from .models import Shift
from .forms import ShiftCreateForm


class ShiftHome(LoginRequiredMixin,View):
    def get(self, request):
        form = ShiftCreateForm()
        return render(request, "shift/manage_shift.html", {'form': form})
    

class ShiftData(LoginRequiredMixin, View):
    def get(self, request):
        shifts = Shift.objects.order_by('-created_at')
        data = []

        for counter, shift in enumerate(shifts, start=1):
            data.append({
                'ID': counter,
                'name': shift.name,
                'short_name': shift.short_name,
                'Time': shift.from_time+"-"+ shift.to_time,
                'duty_hour': shift.duty_hour,
                'Action': f'<a class="btn btn-sm btn-primary btn-edit" data-bs-toggle="modal" data-bs-target="#addEmployeeModal" data-empid="{shift.id}">Edit</a>'
                          f'<a class="ms-3 btn-danger btn btn-sm btn-delete" data-empid="{shift.id}">DEL</a>'
            })

        if data:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'message': 'No Record Found in Database'})