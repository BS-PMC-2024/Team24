from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='HomePage'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='Login'),
    path('support/', views.support, name='support'),
    path('feedback/', views.feedback, name='feedback'),
    path('studentDash/', views.studentDash, name='studentDash'),
    path('clientDash/', views.clientDash, name='clientDash'),
    path('adminDash/', views.adminDash, name='adminDash'),

]
