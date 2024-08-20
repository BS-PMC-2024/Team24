# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,SRS,SupportRequest
from django.db import IntegrityError
from django.shortcuts import render

from django.shortcuts import redirect
from .models import SupportTicket



def admin_feedback(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'admin_feedback.html', context)

def home(request):
    if request.GET.get('action') == 'logout':
        request.session.flush()
        messages.success(request, 'You have been logged out successfully.')
        return redirect('hometest')
    
    print("Session data:", request.session.items())
    print("Is user logged in?", 'user_id' in request.session)
    print("Is student?", request.session.get('is_student'))
    return render(request, 'users/hometest.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_student = request.POST.get('student') == 'yes'  # Capture the student status

        try:
            user = User(username=username, email=email, password=password, is_student=is_student)
            user.save()
            messages.success(request, 'Sign up successful!')
            return redirect('login')  # Redirect to the login page after successful sign-up
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

def want(request):
    return render(request, 'users/WantToKnowMore.html')

def support(request):
    support_requests = SupportRequest.objects.all().order_by('-username')  # Order by username descending
    context = {
        'support_requests': support_requests
    }
    return render(request, 'support.html', context)

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
