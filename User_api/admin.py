from django.contrib import admin
from .models import CustomUser
# admin.site.register(Category


class  CustomUserAdmin(admin.ModelAdmin):
    list_filter = ("id",)
    
  
admin.site.register(CustomUser, CustomUserAdmin)


