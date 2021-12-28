from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import UserAddressAPIView,PostView
from .import views
# from users_api.views import MyObtainTokenPairView



urlpatterns = [
    path('useraddresses/', PostView.as_view(), name='blogs'),
    path('useraddresses/',UserAddressAPIView.as_view(),name="useraddresses"),
    path('',views.database2, name='Homepage'),

]