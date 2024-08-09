# ReqGenius/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

   
urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('', include('users.urls')),  # Include URLs from the users app
  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
