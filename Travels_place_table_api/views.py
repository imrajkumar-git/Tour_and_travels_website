

# Create your views here.
from django.db.models import query
from itsdangerous import Serializer
from rest_framework import permissions
from rest_framework import response
from Travels_Blogs.models import Travels_Blogs_Comment
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Travels_place_table.models import(
Departure_Month, 
Suitable_Date, Travels_Package_Booking, Travelsplacesinformation,
TravelsPlacePath,Travels_category, User_rating, travels_package,
Highlights,Cost_Details,Suitable_Places
)
from Travels_Blogs.models import Travels_Blogs,Travels_Blogs_Gallery,Travels_Blogs_category,Wishlist

from .serializers import(Cost_Details_serializer, Departure_Date_Serializer,
Departure_Month_Serializer, Highlights_serializer, Suitable_places_serializer, 
Travels_Blogs_Serializer,
travels_package_serializer, Travels_places_Serializer,
Travels_Place_Path_serializer,
Travels_Place_category_serializer, User_Rating_serializer,
Cost_Details_serializer,Highlights_serializer,Suitable_places_serializer,
Travels_Blogs_Serializer,Travels_Blogs_Comment_serializer,Travels_blogs_image_serializer,
Travels_blogs_category_serializer,Wishlist_serializer
)

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpResponseRedirect, request
from django.contrib import messages
from django.views.generic import ListView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from User_api.models import CustomUser
from rest_framework.decorators import api_view


class ActionBasedPermission(AllowAny):
    def has_permission(self,request,view):
        for klass,actions in getattr(view,'action_permissions',[]).items():
            if view.action in actions:
                return klass().has_permission(request,view)
            return False

class Travel_Places_Information_ViewSet(viewsets.ModelViewSet):
    queryset = Travelsplacesinformation.objects.all()
    serializer_class = Travels_places_Serializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','travel_place_title','duration','slug','Travels_Category']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }

class Travel_Places_path_ViewSet(viewsets.ModelViewSet):
   
    queryset = TravelsPlacePath.objects.all()
    serializer_class = Travels_Place_Path_serializer
    lookup_field = 'travel_type'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','route_name','travels_place_information']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }
class Travel_Places_category_ViewSet(viewsets.ModelViewSet):
   
    queryset =Travels_category.objects.all()
    serializer_class = Travels_Place_category_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category','id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    


class Wishlist_ViewSet(viewsets.ModelViewSet):
   
    queryset =Wishlist.objects.all()
    serializer_class = Wishlist_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['User','travels_place_information','id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    

   


class Departure_Date_ViewSet(viewsets.ModelViewSet):
   
    queryset =Suitable_Date.objects.all()
    serializer_class = Departure_Date_Serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','travels_place_information','Month','From']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    
    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Your Package is successfully booked:"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
 

class Departure_Month_ViewSet(viewsets.ModelViewSet):
   
    queryset =Departure_Month.objects.all()
    serializer_class = Departure_Month_Serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','travels_place_information']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }

class Rating_ViewSet(viewsets.ModelViewSet):
   
    queryset =User_rating.objects.all()
    serializer_class = User_Rating_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','user','Rating']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    
    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Rating is Sucessfully Submitted"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class Highlights_ViewSet(viewsets.ModelViewSet):
   
    queryset =Highlights.objects.all()
    serializer_class = Highlights_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','travels_place_information']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    


class Suitable_places_ViewSet(viewsets.ModelViewSet):
   
    queryset =Suitable_Places.objects.all()
    serializer_class = Suitable_places_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','travels_place_information']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    

class Cost_Details_ViewSet(viewsets.ModelViewSet):
   
    queryset =Cost_Details.objects.all()
    serializer_class = Cost_Details_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','travels_place_information']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    


class Package_ViewSet(viewsets.ModelViewSet):
   
    queryset =travels_package.objects.all()
    serializer_class = User_Rating_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }    
    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Your Rating is sucessfully Submitted:"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class Travels_blogs_viewSet(viewsets.ModelViewSet):
    
    queryset =Travels_Blogs.objects.all()
    serializer_class = Travels_Blogs_Serializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['Blog_Title','slug','id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
        IsAuthenticated:['put'],

    


    } 
    # def put(self,request, *args, **kwargs):
    #     Serializer=Travels_Blogs_Serializer(data=request.data)
    #     if Serializer.is_valid():
    #         Serializer.update()
    #         return Response(Serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    
class Travels_blogs_Comment_viewSet(viewsets.ModelViewSet):
    
    queryset =Travels_Blogs_Comment.objects.all()
    serializer_class = Travels_Blogs_Comment_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }  
    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Your comment is submitted sucessfully!"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


    
    
class Travels_blogs_image_viewSet(viewsets.ModelViewSet):
    
    queryset =Travels_Blogs_Gallery.objects.all()
    serializer_class = Travels_blogs_image_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    } 


class Travels_blogs_category_viewSet(viewsets.ModelViewSet):
    
    queryset =Travels_Blogs_category.objects.all()
    serializer_class = Travels_blogs_category_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    } 




class Package_booking_ViewSet(viewsets.ModelViewSet):
    queryset =Travels_Package_Booking.objects.all()
    serializer_class = travels_package_serializer
    lookup_field = 'travel_category'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }   
    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Your Package is successfully booked"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        destination_name = get_object_or_404(Travelsplacesinformation, pk=request.data['destination_name'])
        if destination_name.is_booked:
            return Response({"response": "destination is already booked"}, status=status.HTTP_200_OK)
        destination_name.is_booked = True
        destination_name.save()
      
        return self.create(request, *args, **kwargs)


@api_view(['GET','POST'])
def hello_world(request):
    if request.method=='GET':
        return Response ({'msg':'this is a GET Request'
        })

    if request.method=="POST":
        print(request.data)
        return Response({'msg':'this is a POST Request','data':request.data})

#def order_details(request):
    #items = CartItems.objects.filter(user=request.user, ordered=True,status="Active").order_by('-ordered_date')
  # bill = items.aggregate(Sum('item__price'))
   # number = items.aggregate(Sum('quantity'))
   ###total = bill.get("item__price__sum")
   # count = number.get("quantity__sum")
   # total_pieces = pieces.get("item__pieces__sum")
   # context = {
      #  'items':items,
   #     'cart_items':cart_items,
       ### 'total': total,
       # 'count': count,
       # 'total_pieces': total_pieces
    #}
#return render(request, 'main/order_details.html', context)"




class MenuListView(ListView):
    model = Travelsplacesinformation
    template_name = 'Travels_place_information.html'
    context_object_name = 'menu_items'

