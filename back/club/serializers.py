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

class ClubArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_article
        exclude = ('created_at','updated_at'),