from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import CustomUserManager


# Create your models here.

AUTH_PROVIDERS = {'email': 'email'}

    
class CustomUser(AbstractUser):

    Gender=(
        ("1","Male"),
        ("2","Female"),
        ("3","Others"),
    )
    username = models.CharField(max_length=20 ,default="name")
    email = models.EmailField(_('email address'), unique=True)
    contactno = models.CharField(max_length=50,default="9841989898",null=False)
    Profile_Image = models.ImageField(upload_to='user/%Y/',default='/profile_icon/1.jpg')
    Address_line1=models.CharField(max_length=1000,default="Locality/Houses/Street No",null=False)
    Address_line2=models.CharField(max_length=1000,default="Village/City Name",null=False)
    State=models.CharField(max_length=1200,default="Enter your State name",null=False)
    Postal_Code=models.IntegerField(default="356",null=False)
    Country=models.CharField(max_length=1000,default="Nepal",null=False)
    Date_of_Birth=models.DateField(default='2021-12-27',null=False)
    Gender=models.CharField(max_length=1000, choices=Gender,default="Enter your Gender",null=False)
    Country_code=models.IntegerField(default="2500",null=False)


    is_verified = models.BooleanField(default=False)
    address=models.CharField(max_length=30,default="kathmandu")
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    def tokens(self):
        print("inside token")
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }  

