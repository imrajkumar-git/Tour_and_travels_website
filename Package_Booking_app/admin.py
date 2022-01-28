from django.contrib import admin
from .models import (
    Departure_Date,
    Booking,

)


def update_date_is_booked_to_false(model_admin, request, query_set):
    query_set.update(is_booked=False)


update_date_is_booked_to_false.short_description_message = "Update all is_booked to False"




class dateAdmin(admin.ModelAdmin):

    class Meta:
        model = Departure_Date

    list_display = ['__str__', 'is_booked']    
    actions = [update_date_is_booked_to_false]


admin.site.register(Departure_Date, dateAdmin)

admin.site.register(Booking)

