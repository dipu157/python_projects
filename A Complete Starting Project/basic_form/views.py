from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BaseFormCreateForm



class BasicFormIndex(LoginRequiredMixin,View):
    def get(self, request):
        form = BaseFormCreateForm()
        return render(request, "backend/basicForm/basic_form.html", {'form': form})
