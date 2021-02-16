from django.db import models
from django.conf import settings

class Club(models.Model):
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length=50)
    content = models.TextField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True,null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Club_article(models.Model):
    category = models.CharField(max_length=50)
    comment = models.TextField()
    url = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_club_articles')
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    site_name = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=150,blank=True)
    image = models.CharField(max_length=150,blank=True)
    video = models.CharField(max_length=150,blank=True)
    

class Club_member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_club_member_articles')
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    signdate = models.CharField(blank=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    visitdate = models.DateTimeField(auto_now=True)
    visit_cnt = models.IntegerField(default=0)
    article_cnt = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    