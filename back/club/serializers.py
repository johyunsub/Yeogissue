from rest_framework import serializers
from .models import Club, Club_article, Club_member


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
        
class ClubNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('name',)


class ClubInfoSerializer(serializers.ModelSerializer):
    mastername = serializers.CharField(source='master.nickname')
    member_cnt = serializers.IntegerField(source='club_member_set.count')

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
        # fields = '__all__'
        exclude = ('site_name', 'title', 'description', 'image', 'video',)


class ClubArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.nickname')

    class Meta:
        model = Club_article
        fields = '__all__'


class ClubArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_article
        fields = ('category', 'comment', 'url')


class ClubMemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='user.nickname'
    )

    class Meta:
        model = Club_member
        # exclude = ('user',)
        fields = '__all__'
