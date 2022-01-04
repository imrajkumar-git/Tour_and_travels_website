from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import RegisterView,VerifyEmail,LoginAPIView,UserAPIView
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user',UserAPIView,basename="User_api")


urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('email-verify/',VerifyEmail.as_view(),name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls