from django.db import models
import datetime
import os
# Create your models here.

def get_file_path(instance, filename):
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # Get the extension of the original file
    extension = filename.split('.')[-1]
    # Create a new filename using the current time and the original extension
    filename = "%s.%s" % (nowTime, extension)
    return os.path.join('uploads/', filename)


class Genre(models.Model):
    name = models.CharField(max_length=150 ,null =False, blank= False)
    status = models.BooleanField(default=False,help_text= "0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text= "0=default, 1=trending")
    meta_keywords= models.CharField(max_length=150, null=False,blank=False)
    created_At = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    release_Date = models.DateField()
    genre = models.ManyToManyField(Genre)
    name = models.CharField(max_length=150 ,null =False, blank= False)
    product_image = models.ImageField(upload_to=get_file_path, null =True,blank = True)
    product_description = models.TextField(max_length=250,null =False, blank = False)
    quantity = models.IntegerField(null=False,blank = False)
    original_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text= "0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text= "0=default, 1=trending")
    tag = models.CharField(max_length=150,null=False,blank=False)
    meta_title= models.CharField(max_length=150, null=False,blank=False)
    meta_keywords= models.CharField(max_length=150, null=False,blank=False)
    meta_description = models.TextField(max_length=500,null =False, blank = False)
    created_At = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    