from re import search
from django.contrib import admin
from django.db.models.base import Model
from .models import( 
Suitable_Date,
Departure_Month,
Travelsplacesinformation,
TravelsPlacePath,
User_rating,
travels_package,
Travels_Package_Booking)



def update_package_is_booked_to_false(model_admin, request, query_set):
    query_set.update(is_booked=False)


update_package_is_booked_to_false.short_description_message = "Update all is_booked to False"


class Travels_places_information(admin.ModelAdmin):
    list_display = ('id','__str__','is_booked')
    list_filter = ("slug",)
    search_fields = ['user_id']
    fieldsets = [
        ("category", {'fields': ["Travels_category"]}),
        ("Title", {'fields': ["travel_place_title"]}),
        ("max_group_size", {'fields': ["max_group_size"]}),
        ("Age_range", {'fields': ["Age_range"]}),
        ("operate_language", {'fields': ["operate_language"]}),
        ("travels_place_images", {'fields': ["travels_place_image"]}),
        ("", {'fields': ["travels_place_image1"]}),
        ("", {'fields': ["travels_place_image2"]}),
        ("Tour_operator", {'fields': ["Tour_operator"]}),
        ("duration", {'fields': ["duration"]}),
        ("created_on", {'fields': ["created_on"]}),
        ("updated_on", {'fields': ["updated_on"]}),
        ("Total_cost", {'fields': ["Total_cost"]}),
        ("discount", {'fields': ["discount"]}),
        ("slug", {'fields': ["slug"]}),
        ("map", {'fields': ["map"]}),
        ("is_booked",{'fields':["is_booked"]}),

    ]
admin.site.register(Travelsplacesinformation, Travels_places_information)


class TravelsPlace(admin.ModelAdmin):
    search_fields = ['user_id']
    list_display = ('Tour_id','travels_place_information','route_name','route_information')

  
admin.site.register(TravelsPlacePath,TravelsPlace)


class month(admin.ModelAdmin):
    search_fields = ['id']

admin.site.register(Departure_Month,month)

class Day(admin.ModelAdmin):
    search_fields = ['id']
    list_display=('id','From')

admin.site.register(Suitable_Date,Day)

class rating(admin.ModelAdmin):
    search_fields=['id']
    list_display=('user','Rating')
admin.site.register(User_rating,rating)

class Travels_package(admin.ModelAdmin):
    search_fields=['id']
admin.site.register(travels_package,Travels_package)


class travels_place_booking(admin.ModelAdmin):
    list_display=['id','destination_name','checking_date']
admin.site.register(Travels_Package_Booking,travels_place_booking)

