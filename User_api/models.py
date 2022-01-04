from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import CustomUserManager


# Create your models here.

AUTH_PROVIDERS = {'email': 'email'}

    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20 ,default="name")
    email = models.EmailField(_('email address'), unique=True)
    contactno = models.CharField(max_length=50,default="9841989898",null=False)
    Profile_Image = models.ImageField(upload_to='user/%Y/',default='/profile_icon/1.jpg')
    is_verified = models.BooleanField(default=False)

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

