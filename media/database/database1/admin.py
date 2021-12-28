from django.contrib import admin
from .models import Database

class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ("id",)
    search_fields = ['name', 'id']
    
  
admin.site.register(Database, DatabaseAdmin)




