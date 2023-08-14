from django.shortcuts import render
from django.views.generic import View
from .models import BasicForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BaseFormCreateForm



class BasicFormIndex(LoginRequiredMixin,View):
    def get(self, request):
        form = BaseFormCreateForm()
        return render(request, "backend/basicForm/basic_form.html", {'form': form})


class BasicFormCreateView(CreateView):
    model = BasicForm
    template_name = "backend/basicForm/basic_form.html"
    fields = ["name", "code", "blood_group", "slug", "description", "image"]