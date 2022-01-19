from django.contrib import admin
from .models import Travels_Blogs,Travels_Blogs_Comment
# Register your models here.
from tinymce.widgets import TinyMCE
from django.db import models



@admin.register(Travels_Blogs)
class PostAdmin(admin.ModelAdmin):
	  formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
   }


class travels_blogs_comment(admin.ModelAdmin):
    list_display=['id','user']
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
   }
admin.site.register(Travels_Blogs_Comment,travels_blogs_comment)    
