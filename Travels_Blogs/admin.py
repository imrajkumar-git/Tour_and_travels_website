from django.contrib import admin
from .models import Travels_Blogs,Travels_Blogs_Comment
# Register your models here.
from tinymce.widgets import TinyMCE
from django.db import models

class Travels_blog(admin.ModelAdmin):
    list_display=['id','Blog_Title']
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
   }
admin.site.register(Travels_Blogs,Travels_blog)    


class travels_blogs_comment(admin.ModelAdmin):
    list_display=['id','author']
    
admin.site.register(Travels_Blogs_Comment,travels_blogs_comment)    
