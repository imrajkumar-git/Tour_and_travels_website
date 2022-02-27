from django.contrib import admin
from .models import Travels_Blogs,Travels_Blogs_Comment,Travels_Blogs_Gallery,Travels_Blogs_category, Wishlist
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


class travels_blog_gallery(admin.ModelAdmin):
    list_display=['id','Title']
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
   }
admin.site.register(Travels_Blogs_Gallery,travels_blog_gallery)   

class Travels_blogs_category(admin.ModelAdmin):
   list_display=['id']
admin.site.register(Travels_Blogs_category,Travels_blogs_category)   

class wishlist(admin.ModelAdmin):
   list_display=['id','User'
   ]
admin.site.register(Wishlist,wishlist)   
   
