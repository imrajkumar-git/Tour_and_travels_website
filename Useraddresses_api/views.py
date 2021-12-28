
from rest_framework import generics,status
from rest_framework.response import Response

from Travels_place_table.models import Travelsplacesinformation
from .serializers import UserAddressSerializer
from Useraddresses.models import userAddresses
from django.shortcuts import render


class UserAddressAPIView(generics.ListAPIView):
    serializer_class = UserAddressSerializer
    models = userAddresses
    queryset = userAddresses.objects.all()

class PostView(generics.ListCreateAPIView):
    queryset = userAddresses.objects.all()
    serializer_class = UserAddressSerializer

def database2(request):


    
    context = {
        'database2':Travelsplacesinformation.objects.all(),
     
    }
 
    return render(request,'index.html',context)

   


