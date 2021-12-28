from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views
from .views import  Departure_Date_ViewSet, MenuListView, Package_booking_ViewSet, Rating_ViewSet, Travel_Places_Information_ViewSet,Travel_Places_path_ViewSet,Travel_Places_category_ViewSet

router = DefaultRouter()
router.register('travel-place-information',Travel_Places_Information_ViewSet,basename="travel_place")
router.register('travel-place-path', Travel_Places_path_ViewSet ,basename="travel_path")
router.register('Travels-category', Travel_Places_category_ViewSet ,basename="travel_category")
router.register('User-Rating', Rating_ViewSet ,basename="User_Rating")
router.register('Travels-place-booking', Package_booking_ViewSet, basename="Package_booking")
router.register('departre-date', Departure_Date_ViewSet, basename="Departuere_Date")


urlpatterns = [
    path('hello/', MenuListView.as_view(), name='Travels_place_information'),
    path('Travels_place_path_data/',views.database1, name='Database'),    
    path('Travels_place_path_data/api/Travels_place_information_data/api/travels_place_path_data/',views.database1, name='Database2'),     
    path('helloword/', views.hello_world),

]
urlpatterns += router.urls
