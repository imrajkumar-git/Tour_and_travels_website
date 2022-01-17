from .models import Departure_Date,  Booking
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departure_Date
        fields = '__all__'

   

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking

        fields = '__all__'
