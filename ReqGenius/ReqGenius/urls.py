from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='HomePage'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='Login'),
]
