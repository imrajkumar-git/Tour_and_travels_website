from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views
from .views import(
Departure_Date_ViewSet, 
Departure_Month_ViewSet,
MenuListView, 
Package_booking_ViewSet,
Rating_ViewSet,
Travel_Places_Information_ViewSet,
Travel_Places_path_ViewSet,
Travel_Places_category_ViewSet,
Suitable_places_ViewSet,
Cost_Details_ViewSet,
Highlights_ViewSet,
Travels_blogs_Comment_viewSet,
Travels_blogs_viewSet,
Travels_blogs_viewSet,
Travels_blogs_image_viewSet,
Travels_blogs_category_viewSet,
Wishlist_ViewSet

)

router = DefaultRouter()
router.register('travel-place-information',Travel_Places_Information_ViewSet,basename="travel_place")
router.register('travel-place-path', Travel_Places_path_ViewSet ,basename="travel_path")
router.register('Travels-category', Travel_Places_category_ViewSet ,basename="travel_category")
router.register('User-Rating', Rating_ViewSet ,basename="User_Rating")
router.register('Travels-place-booking', Package_booking_ViewSet, basename="Package_booking")
router.register('departre-date', Departure_Date_ViewSet, basename="Departuere_Date")
router.register('departure-month', Departure_Month_ViewSet,basename='Departure-month')
router.register('suitable-places', Suitable_places_ViewSet,basename='suitable-places')
router.register('highlights', Highlights_ViewSet,basename='highlights')
router.register('cost-details', Cost_Details_ViewSet,basename='cost-details')
router.register('blogs', Travels_blogs_viewSet,basename='Travels_blogs')
router.register('User-comment', Travels_blogs_Comment_viewSet,basename='Travels_blogs_comment')
router.register('blogs-image',Travels_blogs_image_viewSet,basename="Travels-image")
router.register('blogs-category',Travels_blogs_category_viewSet,basename='blogs-category')
router.register('wishlist',Wishlist_ViewSet,basename='wishlist')

urlpatterns = [
    path('hello/', MenuListView.as_view(), name='Travels_place_information'),
    path('helloword/', views.hello_world),

]
urlpatterns += router.urls
