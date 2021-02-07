from rest_framework import serializers
from .models import Club, Club_article, Club_member

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class ClublistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ('is_private'),


class ClubUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ('master'),

class ClubArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_article
        fields = '__all__'
class ClubArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_article
        fields = '__all__'
        
class ClubArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_article
        fields = ('category','comment','url')

class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_member
        fields = '__all__'