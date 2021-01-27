from rest_framework import serializers
from .models import Article, Hashtag
from django.contrib.auth import get_user_model



class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)
