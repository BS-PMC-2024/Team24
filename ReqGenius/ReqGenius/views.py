from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback, SupportRequest
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



def HomePage(request):
    return render(request, 'Home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    return render(request, 'signup.html')

def Login(request):
    return render(request, 'Login.html')

def home(request):
    return render(request, 'home.html')

# def support(request):
#     if request.method == 'POST':
#         issue = request.POST.get('issue')
#         SupportRequest.objects.create(user=request.user, issue=issue)
#         messages.success(request, 'Technical support request submitted successfully!')
#         return redirect('support')
#     return render(request, 'support.html')

def support(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            issue_content = request.POST.get('issue')
            if issue_content:
                SupportRequest.objects.create(user=request.user, issue=issue_content)
                return JsonResponse({'status': 'success', 'message': 'Support request submitted successfully!'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Please provide the required information.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'You must be logged in to submit a support request.'})
    return render(request, 'support.html')

def feedback(request):
    if request.method == 'POST':
        feedback_content = request.POST.get('feedback')
        # Save feedback
        Feedback.objects.create(user=request.user, content=feedback_content)
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('feedback')
    return render(request, 'feedback.html')

def studentDash(request):
    return render(request, 'student_dashboard.html')

def clientDash(request):
    return render(request, 'client_dashboard.html')

def adminDash(request):
    feedbacks = Feedback.objects.all()
    support_requests = SupportRequest.objects.all()
    context = {
        'feedbacks': feedbacks,
        'support_requests': support_requests,
    }
    return render(request, 'admin_dashboard.html', context)

# def submit_feedback(request):
#     if request.method == 'POST':
#         feedback_content = request.POST.get('feedback')
#         # Save feedback
#         Feedback.objects.create(user=request.user, content=feedback_content)
#         messages.success(request, 'Feedback submitted successfully!')
#         return redirect('studentDash')  # או redirect לכתובת אחרת אם דרוש
#     return render(request, 'student_dashboard.html')


# def submit_support_request(request):
#     if request.method == 'POST':
#         issue_content = request.POST.get('issue')
#         if issue_content:
#             SupportRequest.objects.create(user=request.user, issue=issue_content)
#             return JsonResponse({'status': 'success', 'message': 'Support request submitted successfully!'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Please provide the required information.'})
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})




