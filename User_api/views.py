from django.http import response
from django.shortcuts import render
from rest_framework import generics,status
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from .utils import Util

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email= user_data['email'])
        print(user)
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        print(relativeLink)
        absurl = 'http://'+ "192.168.10.83:8888" + str(relativeLink) + "?token="+str(token)
        email_body = 'Hi '+user.first_name  +  user.last_name + ' Use the link below to verify your email: '  +  absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        print("i am sending mail")
        Util.send_email(data,)
        print('please check your email: ' + user.email)
        return Response(user_data, status = status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        token = request.GET.get('token')
        try:

            print("i am verifying mail")
            print(token)
            payload = jwt.decode(token, settings.SECRET_KEY,algorithms=['HS256'])
           

            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email':'Successfully activated continue login'},status = status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'Activation Expired'},status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid Token'},status = status.HTTP_400_BAD_REQUEST)


            
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.is_valid)
        return Response(serializer.data, status=status.HTTP_200_OK)

   

class ActionBasedPermission(AllowAny):
    def has_permission(self,request,view):
        for klass,actions in getattr(view,'action_permissions',[]).items():
            if view.action in actions:
                return klass().has_permission(request,view)
            return False



class UserAPIView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']

    permission_classses=[IsAuthenticated]
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update'],
    }    
