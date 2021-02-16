from django.db import models

# Create your models here.
class Dailyissue(models.Model):
    date = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    content = models.CharField(max_length=50)


class News(models.Model):
    content = models.CharField(max_length = 50)
    sort = models.CharField(max_length = 10)
    start = models.CharField(max_length = 10)
    
    link = models.CharField(max_length = 150)
    site_name = models.CharField(max_length = 50,blank=True)
    title = models.CharField(max_length = 50,blank=True)
    description = models.CharField(max_length = 300,blank=True)
    image = models.CharField(max_length = 150,blank=True)
    
class Youtube(models.Model):

    content = models.CharField(max_length = 50)
    sort = models.CharField(max_length = 10)
    start = models.CharField(max_length = 10)

    videoId = models.CharField(max_length = 150)
    channelTitle = models.CharField(max_length = 50,blank=True)
    title = models.CharField(max_length = 50,blank=True)
    description = models.CharField(max_length = 150,blank=True)
    thumbnails = models.CharField(max_length = 150,blank=True)
    publishTime = models.CharField(max_length = 150,blank=True)
    
    
    
    
    
    
    
