from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from User_api.models import CustomUser
# Create your models here.

#user address information
class userAddresses(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    addressLine1 = models.CharField(max_length=250,default="your street/tole name", null=False)
    addressLine2 = models.CharField(max_length=250,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    province = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,default= "Nepal",null=False)
    phone_number = models.CharField(max_length=100,default="phonenumbers",null=False)
  

  