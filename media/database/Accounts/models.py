from django.db import models
class account(models.Model):
# Create your models here.
     name=models.CharField(max_length=100)
     img= models.ImageField('Upload_to=templates')
     desc= models.TextField()
     offer=models.BooleanField(default=False)
    