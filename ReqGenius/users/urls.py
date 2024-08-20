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
    path('feedback.html', views.feedback, name='feedback_html'),
    path('srsinfo/', views.srsinfo, name='srsinfo'),
    # path('srsinfo.html', views.srsinfo, name='srsinfo_html'),
    path('err/', views.err, name='err'),
    path('err.html', views.err, name='err_html'),
    path('srsnew/', views.srsnew, name='srsnew'),
    path('about/', views.about, name='about'),
    path('student-dashboard/', views.dashStudent, name='dashStudent'),
    path('client-dashboard/', views.dashClient, name='dashClient'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('want/', views.want, name='want'),

     # נתיב עבור ניהול התכנים
    #path('adminhome/remove-content/<int:content_id>/', views.remove_educational_content, name='remove_content'),
    #path('stud_view_content/', views.view_educational_content, name='stud_view_content')
    path('admin_manage_content/', views.add_educational_content, name='admin_manage_content'),
    path('remove_content/<int:content_id>/', views.remove_educational_content, name='remove_content'),
    path('view_content/', views.view_educational_content, name='view_content'),
    path('add_zoom_meeting/', views.add_zoom_meeting, name='add_zoom_meeting'),
    path('remove_zoom_meeting/<int:meeting_id>/', views.remove_zoom_meeting, name='remove_zoom_meeting'),



   

]

