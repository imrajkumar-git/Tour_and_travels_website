from typing import Callable, DefaultDict
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.utils.translation import ugettext_lazy as _
from rest_framework.fields import ModelField, SlugField
from User_api.models import CustomUser
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator
from django.contrib import admin
from django.utils.html import format_html

class Travels_category(models.Model):
    category=models.CharField(max_length=200,db_index=True,default="regular")

    def __str__(self):
        return self.category   

class travels_package(models.Model):
    Travels_package_category=models.CharField(max_length=45,null=True)

    def __str__(self):
       return self.Travels_package_name

# class User(models.Model):
#     User_name=models.CharField(max_length=25,null=True,default="Ram")

# def __str__(self):
#         return self.User_name 

#travelsplacepathdetails
class Travelsplacesinformation(models.Model):
    From=models.CharField(max_length=25,null=True)
    To=models.CharField(max_length=30,null=True)
    Max_Evaluation=models.IntegerField(default="2000")
    Difficulty_level=models.CharField(max_length=25,null=True)
    Total_cost=models.IntegerField(null=False,default="1000",validators=[MaxValueValidator(100000),MinValueValidator(1000)])
    discount=models.IntegerField(validators=[MaxValueValidator(90),MinValueValidator(0)], null=False,default="10%")
    Travels_category=models.ForeignKey(Travels_category,null=True,on_delete=models.CASCADE)
    travel_place_title = models.CharField(null=False, blank=False,max_length=250,default='Dhading Simle Trek')
    Tour_operator=models.CharField(max_length=25,default="stravels")
    max_group_size=models.IntegerField(default="10",null=False)
    Age_range=models.IntegerField(default="12")
    operate_language=models.CharField(max_length=20,default="english")
    travels_place_image = models.ImageField(upload_to='places/%Y/%m/', blank=False,null=True)
    travels_place_image1 = models.ImageField(upload_to='places/%Y/%m/', blank=False,null=True)
    travels_place_image2 = models.ImageField(upload_to='places/%Y/%m/', blank=False,null=True)
    duration = models.CharField( max_length=20, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True,null=True)
    created_on = models.DateTimeField(blank=True)
    slug= models.SlugField(max_length=200)
    map=models.TextField(null=True)
    is_booked = models.BooleanField(default=False)

 
    def __str__(self):
        return self.travel_place_title

class TravelsPlacePath(models.Model):
    Tour_id=models.PositiveBigIntegerField(null=True)
    travels_place_information= models.ForeignKey(Travelsplacesinformation,related_name='Travels_place_path',null=True,on_delete=models.CASCADE)
    route_name = models.CharField(max_length=200, db_index=True,default='pokhara')

    route_information=models.TextField(null=False)
    route_picture=models.ImageField(upload_to='places/',blank=True,null=True)

    def __str__(self):
        return self.route_name

    ordering=['Tour_id']    

#from tour_and_travels.settings import DATE_INPUT_FORMATS



#user Places information


class Departure_Month(models.Model):
    

    travels_place_information= models.ForeignKey(Travelsplacesinformation,related_name='departure_Month',null=True,on_delete=models.CASCADE)
    month_name = models.CharField(max_length=50)

    def __str__(self):
        return self.month_name

class Suitable_Date(models.Model):
    Day_Name=(
        ("1","Sunday"),
        ("2","Monday"),
    )

    From=models.DateField(null=True)
    travels_place_information= models.ForeignKey(Travelsplacesinformation,related_name='departure_Date',null=True,on_delete=models.CASCADE)

    TO=models.DateField(null=True)
    Month = models.ForeignKey(Departure_Month, on_delete=models.CASCADE, related_name='suitable_date', null=True, blank=True)
    day_name = models.CharField(max_length=100)


    #categoryPart

class User_rating(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    travels_place_information= models.ForeignKey(Travelsplacesinformation,related_name='user_rating',null=True,on_delete=models.CASCADE)
    Rating=models.IntegerField(validators=[MinValueValidator(0),
                                        MaxValueValidator(500)],null=True)
    Rating_Description=models.TextField(null=True)                                    
                  

def __str__(self):
    return self.Rating


class Travels_Package_Booking(models.Model):
    destination_name=models.ForeignKey(Travelsplacesinformation,null=False,on_delete=models.CASCADE,default='2')
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=False,default='41')
    checking_date = models.DateField(blank=True,null=False,default='2021-12-23')
    is_booked=models.BooleanField(null=False,default='True')
    check_out_date=models.DateField(blank=True,null=False,default='2021-12-27')
    No_of_people=models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(20)],null=False,default='3')


def __str__(self):
    return self.destination.destination
    

class Suitable_Places(models.Model):
    Image=models.ImageField(upload_to='places/Suitable_places',blank=True,null=True)  
    Image1=models.ImageField(upload_to='places/Suitable_places',blank=True,null=True)  
    Image2=models.ImageField(upload_to='places/Suitable_places',blank=True,null=True)  
    Image3=models.ImageField(upload_to='places/Suitable_places',blank=True,null=True)  
    Image4=models.ImageField(upload_to='places/Suitable_places',blank=True,null=True)  
    travels_place_information=models.ForeignKey(Travelsplacesinformation,null=False,on_delete=models.CASCADE)

class Highlights(models.Model):
   Highlights=models.TextField(null=True)
   travels_place_information=models.ForeignKey(Travelsplacesinformation,null=False,on_delete=models.CASCADE)


class Cost_Details(models.Model):
    Cost_Details=models.TextField(null=True)
    travels_place_information=models.ForeignKey(Travelsplacesinformation,null=False,on_delete=models.CASCADE)


