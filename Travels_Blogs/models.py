from django.db import models
from User_api.models import CustomUser


# Create your models here.
class Travels_Blogs_category(models.Model):
    Blogs_Category=models.CharField(max_length=2000,null=False,default="category")

class Travels_Blogs(models.Model):
    Blog_Title=models.CharField(max_length=36,null=False,default="pokhara")
    Blog_category=models.ForeignKey(Travels_Blogs_category, on_delete=models.CASCADE,null=True)
    User=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    Blog_Description=models.TextField(null=True)
    Image=models.ImageField(upload_to='Travels_Blogs/pictures',blank=True,null=False,default='/profile_icon/1.jpg')  
    slug=models.SlugField(null=False,default="pkr")
    summary=models.CharField(max_length=2000,null=False,default="your own word")

    def __str__(self):
        return self.Blog_Title


class Travels_Blogs_Comment(models.Model):
        Travels_Blogs=models.ForeignKey(Travels_Blogs,on_delete=models.CASCADE,null=True)

        user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
        comments=models.TextField(null=False,default="your own content")
        created_on = models.DateTimeField(blank=True,auto_now=True)
        updated_on = models.DateTimeField(blank=True,null=True,auto_now=True)

        def __str__(self):
            return self.author.username    

class Travels_Blogs_Gallery(models.Model):
    Title=models.CharField(max_length=35,null=False,default="Our own title")
    User=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    updated_on = models.DateTimeField(blank=True,null=True,auto_now=True)
    Image=models.ImageField(upload_to='Travels_Blogs/pictures',blank=True,null=False,default='/profile_icon/1.jpg')  

    def __str__(self):
        return self.Title


