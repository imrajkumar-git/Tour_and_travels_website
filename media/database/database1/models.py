from django.db import models
    
class Database(models.Model):
    name = models.CharField(max_length=1000, db_index=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    vendor = models.CharField(max_length=200, db_index=True)
    remarks = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name
        