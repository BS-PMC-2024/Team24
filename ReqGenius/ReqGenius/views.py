# from django.http import HttpResponse
from django.shortcuts import render
def HomePage(request):
    # return HttpResponse("Hello")
    return render(request, 'Home.html')
def about(request):
    # return HttpResponse("My about")
    return render(request, 'about.html')
<<<<<<< HEAD
def signup(request):
    # return HttpResponse("My about")
    return render(request, 'signup.html')
=======
def Login(request):
    # return HttpResponse("Login")
    return render(request, 'Login.html')
>>>>>>> 16863f2034637e92d04f19e7b067f040f54163f2
