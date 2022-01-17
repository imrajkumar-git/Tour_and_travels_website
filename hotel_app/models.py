from django.db import models
from User_api.models import CustomUser
from Travels_place_table.models import Travelsplacesinformation,Departure_Month

class Departure_Date(models.Model):
    destination=models.ForeignKey(Travelsplacesinformation,on_delete=models.CASCADE,null=True)
    month_name = models.ForeignKey(Departure_Month,on_delete=models.CASCADE,null=True)
    To = models.DateField(null=True, blank=True)
    From = models.DateField(blank=True, null=True)

    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.month_name.month_name




class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.ForeignKey('Departure_Date', on_delete=models.CASCADE)
    From = models.DateField(blank=True, null=True)
    To = models.DateField(null=True, blank=True)
    No_of_people = models.DecimalField(max_digits=8, decimal_places=3,null=True)

  


    def __str__(self):
        return self.customer.first_name
        
