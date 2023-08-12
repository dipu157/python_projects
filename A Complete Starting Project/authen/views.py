from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "registration/signup.html"

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section': 'dashboard'})

@login_required
def profile(request):
    return render(request,'profile.html',{'section': 'profile'})
