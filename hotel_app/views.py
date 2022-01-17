from django.shortcuts import get_object_or_404
from .models import  Booking, Departure_Date
from .serializer import RoomSerializer, BookingSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ActionBasedPermission(AllowAny):
    def has_permission(self,request,view):
        for klass,actions in getattr(view,'action_permissions',[]).items():
            if view.action in actions:
                return klass().has_permission(request,view)
            return False

class RoomView(viewsets.ModelViewSet):
   
    serializer_class = RoomSerializer
    queryset = Departure_Date.objects.order_by('-id')
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    permissions_classes = (ActionBasedPermission)
    action_permissions = {
        IsAdminUser : ['update','create','destroy','partial_update'],
        AllowAny : ['list','retrieve'],
    }
    
class RoomDetailView(RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Departure_Date.objects.all()
    lookup_field = 'room_slug'


class BookingCreateApiView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Departure Date is successfully booked"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        date = get_object_or_404(Departure_Date, pk=request.data['date'])
        if date.is_booked:
            return Response({"response": "This Departure is already booked try another"}, status=status.HTTP_200_OK)
        date.is_booked = True
        date.save()
      
        return self.create(request, *args, **kwargs)

