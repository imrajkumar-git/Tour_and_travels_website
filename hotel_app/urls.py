from django.contrib import admin
from django.urls import path, include
from .views import RoomView,BookingCreateApiView
from rest_framework.routers import DefaultRouter

app_name = 'hotel_app'

router = DefaultRouter()
router.register('get-list',RoomView,basename="Roomview")
urlpatterns = [
    path('book/', BookingCreateApiView.as_view(), name='book_room'),
  
]
urlpatterns += router.urls
