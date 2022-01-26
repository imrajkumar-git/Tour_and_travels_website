from django.db import models
from User_api.models import CustomUser
from Travels_place_table.models import Travels_category

# Create your models here.
class Travels_Blogs_category(models.Model):
    Blogs_Category=models.CharField(max_length=2000,null=False,default="category")
 

    def __str__(self):
        return self.Blogs_Category

class Travels_Blogs(models.Model):
    Blog_Title=models.CharField(max_length=36,null=False,default="pokhara")
    Blog_category=models.ForeignKey(Travels_Blogs_category, on_delete=models.CASCADE,null=True)
    User=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    Blog_Description=models.TextField(null=True)
    Image=models.ImageField(upload_to='Travels_Blogs/pictures',blank=True,null=False,default='/profile_icon/1.jpg')  
    slug=models.SlugField(null=False,default="pkr")
    summary=models.CharField(max_length=2000,null=False,default="your own word")
    created_on = models.DateTimeField(blank=True,auto_now=True)
    updated_on = models.DateTimeField(blank=True,null=True,auto_now=True)
    def __str__(self):
        return self.Blog_Title


class Travels_Blogs_Comment(models.Model):
        Travels_Blogs=models.ForeignKey(Travels_Blogs,on_delete=models.CASCADE,null=True)

        user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
        comments=models.TextField(null=False,default="your own content")
        created_on = models.DateTimeField(blank=True,auto_now=True)
        updated_on = models.DateTimeField(blank=True,null=True,auto_now=True)

        def __str__(self):
            return self.user.username    

class Travels_Blogs_Gallery(models.Model):
    Title=models.CharField(max_length=35,null=False,default="Our own title")
    User=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    updated_on = models.DateTimeField(blank=True,null=True,auto_now=True)
    Image=models.ImageField(upload_to='Travels_Blogs/pictures',blank=True,null=False,default='/profile_icon/1.jpg')  

    def __str__(self):
        return self.Title

class Wishlist(models.Model):
        Title=models.CharField(max_length=3500,null=False,default="Our own title")
        category=models.ForeignKey(Travels_Blogs_category,on_delete=models.CASCADE,null=False)
        Activity_Level=models.CharField(max_length=1000,default="Modarate",null=False)
        Age=models.IntegerField(default="14+",null=False)
        Duration=models.CharField(max_length=200,default="14D",null=False)

        def __str__(self):
            return self.Title


class Article(models.Model):
        Title=models.CharField(max_length=3500,null=False,default="Our own title")
        summary=models.CharField(max_length=7500,null=False,default="Our own title")
        category=models.ForeignKey(Travels_Blogs_category,on_delete=models.CASCADE,null=False)
        content=models.TextField(default="write your own content",null=False)
        Image=models.ImageField(upload_to='Article/',blank=True,null=False,default='/profile_icon/1.jpg')  

        def __str__(self):
            return self.Title