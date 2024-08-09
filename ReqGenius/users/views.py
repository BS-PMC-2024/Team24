# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.db import IntegrityError
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib import messages
from .models import SupportTicket



def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_student = request.POST.get('is_student') == '1'

        try:
            user = User(username=username, email=email, password=password, is_student=is_student)
            user.save()
            messages.success(request, 'Sign up successful!')
            return redirect('login')  # Redirect to the home page after successful sign-up
        except IntegrityError:
            messages.error(request, 'Username or email already exists.')

    return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username, password=password)     
            return redirect('login')
        except User.DoesNotExist:
            # Login failed
            messages.error(request, 'Login failed. Please check your username and password.')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')

from django.shortcuts import render

from django.shortcuts import render

def support(request):
    return render(request, 'users/support.html')

def feedback(request):
    return render(request, 'users/feedback.html')


def srsinfo(request):
    return render(request, 'users/srsinfo.html')

def err(request):
    return render(request, 'users/err.html')

from django.shortcuts import render

def srs(request):
    return render(request, 'users/srs.html')  
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    return render(request, 'users/about.html')

@login_required
def dashStudent(request):
    return render(request, 'dashStudent.html')

@login_required
def dashClient(request):
    return render(request, 'dashClient.html')
