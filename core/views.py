from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ApplicantForm
from .models import Applicant
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ApplicantForm()
    return render(request, 'core/register.html', {'form': form})



def thank_you(request):
    return render(request, 'core/thank_you.html')

@login_required(login_url='login')
def admin_view(request):
    applicants = Applicant.objects.all().order_by('-submitted_at')
    return render(request, 'core/admin_view.html', {'applicants': applicants})

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('admin_view')
        else:
            error = "Invalid username or password"
    return render(request, 'core/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

def error_view(request):
    return render(request, 'core/error.html')
