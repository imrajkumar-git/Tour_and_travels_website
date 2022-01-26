from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from User_api.models import CustomUser
from django.contrib import auth
from rest_framework.response import Response

from rest_framework.exceptions import AuthenticationFailed
# from django.db import transaction
# from rest_auth.registration.serializers import RegisterSerializer
class RegisterSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    contactno = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50,min_length=8,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email','contactno','password','first_name','last_name','Address_line1','Address_line2',
        'State','Postal_Code','Country','Date_of_Birth','Gender','Country_code','address','Profile_Image']

    
    def validate(self,attrs):
        return super().validate(attrs)
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','contactno','Profile_Image','first_name','last_name','address']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    tokens = serializers.CharField(max_length=68,min_length=6,read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id','email', 'password', 'tokens']


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        filtered_user_by_email = CustomUser.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)
        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

     
        return {
            'id':user.id,
            'email': user.email,
            'tokens': user.tokens,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'Profile_Image':user.Profile_Image,
        }


