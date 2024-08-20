# users/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='hometest'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('support/', views.support, name='support'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback.html', views.feedback, name='feedback_html'),
    path('srsinfo/', views.srsinfo, name='srsinfo'),
    path('srsinfo.html', views.srsinfo, name='srsinfo_html'),
    path('err/', views.err, name='err'),
    path('err.html', views.err, name='err_html'),
    path('srsnew/', views.srsnew, name='srsnew'),
    path('about/', views.about, name='about'),
    path('student-dashboard/', views.dashStudent, name='dashStudent'),
    path('client-dashboard/', views.dashClient, name='dashClient'),

]

