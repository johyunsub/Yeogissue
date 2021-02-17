from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    scrap_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='scrap_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_type = models.BooleanField()
    category = models.CharField(max_length=100)
    read_count = models.IntegerField(default=0)

    club_pk = models.IntegerField(default=0)
    clubname = models.CharField(default='',max_length = 150)
    
    agree_count = models.IntegerField(default=0)
    disagree_count = models.IntegerField(default=0)

class Hashtag(models.Model):
    name = models.CharField(max_length=100)
    post_cnt = models.IntegerField(default=1)
    articles = models.ManyToManyField(Article,related_name='hashtags')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='user_hashtags')
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    opinion_type = models.BooleanField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    badcomment = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    emotion = models.CharField(max_length = 10)
    

class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    badcomment = models.IntegerField(default=0)
    emotion = models.CharField(max_length = 10)
