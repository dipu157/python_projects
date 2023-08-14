from django.shortcuts import render
from django.views.generic import View
from .models import BasicForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import BaseFormCreateForm



class BasicFormIndex(LoginRequiredMixin,View):
    def get(self, request):
        form = BaseFormCreateForm()
        return render(request, "backend/basicForm/basic_form.html", {'form': form})


class BasicFormCreateView(LoginRequiredMixin, CreateView):
    model = BasicForm
    form_class = BaseFormCreateForm
    template_name = "backend/basicForm/basic_form.html"
    success_url = reverse_lazy('bform_add')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user for the form instance
        response = super().form_valid(form)  # Call the parent class's form_valid method
        messages.success(self.request, 'Form successfully Saved!')
        return response