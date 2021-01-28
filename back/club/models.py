from django.db import models
from django.conf import settings

class Club(models.Model):
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length=50)
    content = models.TextField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Club_article(models.Model):
    comment = models.TextField()
    url = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_club_articles')
    club = models.ForeignKey(Club, on_delete=models.CASCADE)


class Club_member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_club_member_articles')
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
