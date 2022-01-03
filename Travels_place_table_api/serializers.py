from django.core.exceptions import EmptyResultSet, ValidationError
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.routers import SimpleRouter
from User_api.serializers import UserSerializer
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


from Travels_place_table.models import Travels_category,Suitable_Date, Departure_Month, Travels_Package_Booking, Travelsplacesinformation,TravelsPlacePath, User_rating


class User_Rating_serializer(serializers.ModelSerializer):
    class Meta:
        model=User_rating
        fields = "__all__"
    



class Travels_Place_Path_serializer(serializers.ModelSerializer):

    class Meta:
        model= TravelsPlacePath
        fields = [
        'id','Tour_id','route_name',
      'route_information','route_picture','travels_place_information'
        ]    






class Departure_Date_Serializer(serializers.ModelSerializer):
    From=serializers.DateField()
    TO=serializers.DateField()

    class Meta:
        model=Suitable_Date
        fields=('id','Month','From','TO')
 

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
        'id','Total_cost','discount','Travels_category',
        'travel_place_title','Tour_operator',
        'max_group_size','Age_range','operate_language',
        'travels_place_image',
        'travels_place_image1','travels_place_image2',
        'duration','updated_on','created_on','slug','map','Travels_place_path','user_rating','departure_Month',
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
            raise serializers.ValidationError("Check Out date must be greater than Check in date")
        
            
        if int(No_of_people)>20:    
            raise serializers.ValidationError({
                'month_name': 'No_of people must be less then 20 character.'
            })
        if int(No_of_people)<1:
            raise serializers.ValidationError({
                'No_of_people':'No of people can not  be negative'
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
