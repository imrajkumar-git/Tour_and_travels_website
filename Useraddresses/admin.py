from django.contrib import admin
from .models import userAddresses
# admin.site.register(Category


class  userAddressesAdmin(admin.ModelAdmin):
    list_filter = ("id",)
    
  
admin.site.register(userAddresses, userAddressesAdmin)
