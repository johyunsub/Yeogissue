from rest_framework import serializers
from .models import Article, Hashtag, Comment
from django.contrib.auth import get_user_model

class HashtagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hashtag
        fields = '__all__'
        read_only_fields = ('article',)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(
        many=True,
        read_only=True,
    )

    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    
    like_users_count = serializers.IntegerField(
        source='like_users.count',
        read_only=True,
    )

    scrap_users_count = serializers.IntegerField(
        source='scrap_users.count',
        read_only=True,
    )

    class Meta:
        model = Article
        fields = '__all__'
 

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title','user','created_at','read_count','category')



