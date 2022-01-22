from django.core.exceptions import EmptyResultSet, ValidationError
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.routers import SimpleRouter
from Travels_Blogs.models import Travels_Blogs_Comment,Travels_Blogs_Gallery,Travels_Blogs_category
from User_api.serializers import UserSerializer
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


from Travels_place_table.models import(
Travels_category,Suitable_Date, 
Departure_Month, Travels_Package_Booking, 
Travelsplacesinformation,TravelsPlacePath,
User_rating,Suitable_Places,Highlights,Cost_Details

 )
from Travels_Blogs.models import Travels_Blogs 


class User_Rating_serializer(serializers.ModelSerializer):
    Rating=serializers.IntegerField()

    class Meta:
        model=User_rating
        fields = "__all__"
    
    def validate(self, data):
        Rating=data.get('Rating')

        if int(Rating)<0:
            raise serializers.ValidationError({
                'error':'rating can not be negative'

        })
        
        if int(Rating)==0:
            raise serializers.ValidationError({
                'error':'rating can not be Zero'

        })
        
        if int(Rating)>100:
            raise serializers.ValidationError({
                'error':'maximum Rating is 100'

        })
        print('Rating' + Rating + 'is sucessfully submitted')

        return data




class Suitable_places_serializer(serializers.ModelSerializer):
    
    class Meta:
        model= Suitable_Places
        fields = "__all__"                                   
 
        
        

class Cost_Details_serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Cost_Details
        fields = "__all__"                                   
 
        

class Highlights_serializer(serializers.ModelSerializer):
    
    class Meta:
        model= Highlights
        fields = "__all__"                                   
 
        

class Travels_Place_Path_serializer(serializers.ModelSerializer):

    class Meta:
        model= TravelsPlacePath
        fields = [
        'id','Tour_id','route_name',
      'route_information','route_picture','travels_place_information'
        ]    


class Travels_Blogs_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model= Travels_Blogs
        fields = "__all__"                                   
 
class Travels_Blogs_Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model=Travels_Blogs_Comment
        fields = ['id','author','Travels_Blogs','comments','created_on','updated_on']     


class Travels_blogs_image_serializer(serializers.ModelSerializer):
    class Meta:
        model=Travels_Blogs_Gallery
        fields = "__all__"                            


class Travels_blogs_category_serializer(serializers.ModelSerializer):
    class Meta:
        model=Travels_Blogs_category
        fields="__all__"


class Departure_Date_Serializer(serializers.ModelSerializer):
    From=serializers.DateField()
    TO=serializers.DateField()

    class Meta:
        model=Suitable_Date
        fields=('id','Month','From','TO','travels_place_information')
 

    def validate(self, data):

        if data['TO'] <= data['From']:
            raise serializers.ValidationError("Check Our date is  must be greater then Check in")
        
       
        return data

class Departure_Month_Serializer(serializers.ModelSerializer):
    suitable_date=Departure_Date_Serializer(read_only=True,many=True)
    class Meta:
        model=Departure_Month
        fields=('id','travels_place_information','month_name','suitable_date')

   

class Travels_places_Serializer(serializers.ModelSerializer):
    user_rating = User_Rating_serializer(read_only=True,many=True)
    Travels_place_path = Travels_Place_Path_serializer(read_only=True, many=True)
    departure_Month = Departure_Month_Serializer(read_only=True, many=True)
    departure_Date = Departure_Date_Serializer(read_only=True, many=True)
    highlights=Highlights_serializer(read_only=True,many=True)
    cost_details=Cost_Details_serializer(read_only=True,many=True)
    Total_cost=serializers.IntegerField()
    discount=serializers.IntegerField()
   
    Tour_operator=serializers.CharField()
    max_group_size=serializers.IntegerField()
    operate_language=serializers.CharField()
    
    duration = serializers.CharField()
    updated_on = serializers.DateTimeField()
    created_on = serializers.DateTimeField()
    slug= serializers.SlugField()
    map=serializers.CharField()
    class Meta:
        model = Travelsplacesinformation
        fields = [
        'id','Travels_Category','Total_cost','discount',
        'travel_place_title','Overview','Tour_operator','summary',
        'max_group_size','Max_Age_range','Min_Age_range','operate_language',
        'travels_place_image',
        'travels_place_image1','travels_place_image2',
        'duration','updated_on','created_on','slug','map',
        'Difficulty_level','From','To','Max_Evaluation',
        'Travels_place_path','user_rating','highlights','cost_details','departure_Month','departure_Date'
       
        ]


class Travels_Place_category_serializer(serializers.ModelSerializer):
    
    class Meta:
        model= Travels_category
        fields = "__all__"                                   




class travels_package_serializer(serializers.ModelSerializer):
    User_information = UserSerializer(read_only=True, many=True)
    checking_date = serializers.DateField()
    is_booked=serializers.BooleanField()
    check_out_date=serializers.DateField()
    No_of_people=serializers.IntegerField()

    class Meta:
        model=Travels_Package_Booking
        fields = ('id','destination_name','User','No_of_people','checking_date','check_out_date','is_booked','User_information')
    
    def validate(self, data):
        is_booked=data.get('is_booked')
        No_of_people=data.get('No_of_people')

        if data['check_out_date'] <= data['checking_date']:
            raise serializers.ValidationError({
                'error':"Check Out date must be greater than Check in date"
            })
        
            
        if int(No_of_people)>20:    
            raise serializers.ValidationError({
                'error': 'No_of people must be less then 20 character.'
            })
        if int(No_of_people)<1:
            raise serializers.ValidationError({
                'error':'No of people can not  be negative'
            })    
        
       
        if bool(not is_booked):
            raise serializers.ValidationError("package is already booked")   
        return data

    def post(self, request, *args, **kwargs):
        room = get_object_or_404(Travelsplacesinformation, pk=request.data['room'])
        if room.is_booked:
            return Response({"response": "Room is already booked"}, status=status.HTTP_200_OK)
        room.is_booked = True
        room.save()
      
        return self.create(request, *args, **kwargs)
