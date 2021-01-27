from rest_framework import serializers
from .models import Club, Club_article, Club_member
from django.contrib.auth import get_user_model

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class ClublistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ('is_private'),