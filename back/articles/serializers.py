from rest_framework import serializers
from .models import Article, Hashtag, Comment,ReComment
from django.contrib.auth import get_user_model
from club.models import Club
from club.serializers import ClubNameSerializer
class HashtagSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Hashtag
        fields = '__all__'
        # read_only_fields = ('articles',)
class HashtagNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtag
        fields = ('name',)
        

class HashtagSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model = Hashtag
        exclude = ('name',)
        # fields = '__all__'
        # read_only_fields = ('articles',)

class ReCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReComment
        fields = '__all__'
        read_only_fields = ('comment',)

class CommentSerializer(serializers.ModelSerializer):
    recomment_set = ReCommentSerializer(many=True, read_only=True)
    recomment_count = serializers.IntegerField(
        source='recomment_set.count',
        read_only=True,
    )
    like_users_count = serializers.IntegerField(
        source='like_users.count',
        read_only = True,
    )

    # type_count = serializers.IntegerField(
    #     source='opinion_type.count',
    #     read_only=True,
    # )

    username = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article','like_users')

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
    username = serializers.ReadOnlyField(source='user.nickname')
 
    # type_count = serializers.IntegerField(
    #     source='comment_set.data.opinion_type.count',
    #     read_only=True,
    # )

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('like_users','scrap_users')

 


class ArticleListSerializer(serializers.ModelSerializer):
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
    username = serializers.ReadOnlyField(source='user.nickname')
    

    # clubname = ClubNameSerializer(read_only=True)
    # clubname = serializers.CharField(
        
    #     source=clubname(club_pk),
    #     read_only=True, 
    # )

    class Meta:
        model = Article
        exclude = ('like_users','scrap_users')
        
        read_only_fields = ('like_users',)



class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('like_users','scrap_users')