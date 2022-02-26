
from pathlib import Path
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework import routers
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Useraddresses_api.urls')),
    path('router/', include('Travels_place_table_api.urls')),  
    path('api/', include('Useraddresses_api.urls')),
    path('account/',include('User_api.urls')),
    path('api/', include('Travels_place_table_api.urls')),
    url('myapp/', include('myapp.urls')),
    path('tinymce/',include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

