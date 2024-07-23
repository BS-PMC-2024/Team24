from django.shortcuts import render

def HomePage(request):
    return render(request, 'Home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    return render(request, 'signup.html')

def Login(request):
    return render(request, 'Login.html')
