# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,SRS,SupportRequest
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

from django.forms import ValidationError
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback, User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from .models import EducationalContent
from .form import EducationalContentForm



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
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['is_student'] = user.is_student
                messages.success(request, 'You have successfully logged in.')
                
                # Check for specific username and redirect
                if username == 'Hadas Hasidim':
                    return redirect('adminhome')  
                
                return redirect('hometest')
            else:
                messages.error(request, 'Login failed. Incorrect password.')
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Login failed. Username does not exist.')
            return redirect('login')
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

def srs_students(request):
    return render(request, 'users/srs_students.html')

def err(request):
    return render(request, 'users/err.html')

from django.shortcuts import render

class SRSForm(forms.ModelForm):
    class Meta:
        model = SRS
        fields = ['field1', 'field2', 'field3', 'field4', 'field5']
        widgets = {
            'field1': forms.Textarea(attrs={'rows': 4}),
            'field2': forms.Textarea(attrs={'rows': 4}),
            'field3': forms.Textarea(attrs={'rows': 4}),
            'field4': forms.Textarea(attrs={'rows': 4}),
            'field5': forms.Textarea(attrs={'rows': 4}),
        }

from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

@csrf_protect
def srsnew(request):
    username = request.session.get('username')
    if not username:
        return JsonResponse({'status': 'error', 'message': 'No user logged in'})

    srs_instance, created = SRS.objects.get_or_create(username=username)
    
    if request.method == 'POST':
        field = request.POST.get('field')
        value = request.POST.get('value')
        
        if field and field in ['field1', 'field2', 'field3', 'field4', 'field5']:
            setattr(srs_instance, field, value)
            srs_instance.save()
            return JsonResponse({'status': 'success', 'message': f'{field} updated successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid field'})
    
    context = {
        'field1': srs_instance.field1,
        'field2': srs_instance.field2,
        'field3': srs_instance.field3,
        'field4': srs_instance.field4,
        'field5': srs_instance.field5,
    }
    return render(request, 'users/srsnew.html', context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    return render(request, 'users/about.html')



from django.shortcuts import render
from .models import User

def adminhome(request):
    # Handle POST request to delete a user
    if request.method == 'POST':
        user_id = request.POST.get('delete_user')  # Get the user ID from the form
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                user.delete()
                print(f"User with ID {user_id} has been deleted.")
            except User.DoesNotExist:
                print(f"User with ID {user_id} does not exist.")
        
        return redirect('adminhome')  # Redirect to the same page after deletion

    # Fetch users and user count for GET request
    excluded_username = 'Hadas Hasidim'  # Replace with the actual username you want to exclude
    users = User.objects.exclude(username=excluded_username)
    user_count = users.count()

    context = {
        'users': users,
        'user_count': user_count,
    }

    return render(request, 'adminhome.html', context)
def feedback(request):
    if request.method == 'POST':
        user = None
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
        
        feedback = Feedback(
            user=user,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            overall_experience=request.POST.get('overall_experience'),
            ease_of_use=request.POST.get('ease_of_use'),
            functionality=request.POST.get('functionality'),
            visual_design=request.POST.get('visual_design'),
            performance=request.POST.get('performance'),
            additional_comments=request.POST.get('additional_comments'),
            created_at=timezone.now()  
        )
        feedback.save()
        messages.success(request, 'Thank you for your feedback!')
        return redirect('hometest')
    
    initial_data = {}
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        initial_data = {
            'name': user.username,
            'email': user.email
        }
    
    return render(request, 'users/feedback.html', {'initial_data': initial_data})

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings

@csrf_exempt
def support_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        report = request.POST.get('report')
        file = request.FILES.get('file')

        if username and email and report:
            file_url = None
            if file:
                # Save the file and get its URL
                file_name = f"{username}_{file.name}"
                file_path = os.path.join(settings.MEDIA_ROOT, 'support_files', file_name)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                file_url = settings.MEDIA_URL + 'support_files/' + file_name

            # Create and save the SupportRequest object
            support_request = SupportRequest(
                username=username,
                email=email,
                report=report,
                file=file_url
            )
            support_request.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing required fields'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

def add_educational_content(request):
    form = EducationalContentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_manage_content')  # השם של הנתיב
    
    content = EducationalContent.objects.all()
    return render(request, 'users/admin_manage_content.html', {'form': form, 'content': content})

def remove_educational_content(request, content_id):
    content = EducationalContent.objects.get(id=content_id)
    content.delete()
    return redirect('users/admin_manage_content/')

def view_educational_content(request):
    content = EducationalContent.objects.all()
    zoom_meetings = ZoomMeeting.objects.all()
    return render(request, 'users/view_content.html', {'content': content, 'zoom_meetings': zoom_meetings})



from .models import ZoomMeeting

# הוספת מפגש זום
def add_zoom_meeting(request):
    if request.method == 'POST':
        zoom_link = request.POST.get('zoom_link')
        if zoom_link:
            ZoomMeeting.objects.create(url=zoom_link)
        return redirect('admin_manage_content')

# הסרת מפגש זום
def remove_zoom_meeting(request, meeting_id):
    meeting = ZoomMeeting.objects.get(id=meeting_id)
    meeting.delete()
    return redirect('admin_manage_content')