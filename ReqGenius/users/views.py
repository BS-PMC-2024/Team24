# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.shortcuts import redirect
from .models import SupportTicket



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
    return render(request, 'users/support.html')

def feedback(request):
    return render(request, 'users/feedback.html')

def srsinfo(request):
    return render(request, 'users/srsinfo.html')

def err(request):
    return render(request, 'users/err.html')

from django.shortcuts import render

def srsnew(request):
    return render(request, 'users/srsnew.html')  

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

from django.shortcuts import render
from .models import User

def adminhome(request):
    users = User.objects.all()
    user_count = users.count()
    print(f"Number of users: {user_count}")
    context = {
        'users': users,
        'user_count': user_count,
    }
    return render(request, 'adminhome.html', context)


from django.shortcuts import render, redirect
from .models import EducationalContent
from .form import EducationalContentForm

# תצוגה לניהול התכנים על ידי המנהל
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



    


