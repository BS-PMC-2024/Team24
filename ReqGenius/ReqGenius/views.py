# from django.http import HttpResponse
from django.shortcuts import render
def HomePage(request):
    # return HttpResponse("Hello")
    return render(request, 'Home.html')
def about(request):
    # return HttpResponse("My about")
    return render(request, 'about.html')
