# users/urls.py

from django.urls import path
from . import views
from django.urls import path, include




urlpatterns = [
    path('', views.home, name='hometest'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('support/', views.support, name='support'),
    path('feedback/', views.feedback, name='feedback'),
    path('srsnew/', views.srsnew, name='srsnew'),
    path('about/', views.about, name='about'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('want/', views.want, name='want'),
    path('admin_feedback/', views.admin_feedback, name='admin_feedback'),
    path('support-request/', views.support_request, name='support_request'),
    path('srs_students/', views.srs_students, name='srs_students'),
    path('admin_manage_content/', views.add_educational_content, name='admin_manage_content'),
    path('remove_content/<int:content_id>/', views.remove_educational_content, name='remove_content'),
    path('view_content/', views.view_educational_content, name='view_content'),
    path('add_zoom_meeting/', views.add_zoom_meeting, name='add_zoom_meeting'),
    path('remove_zoom_meeting/<int:meeting_id>/', views.remove_zoom_meeting, name='remove_zoom_meeting'),

   

]

