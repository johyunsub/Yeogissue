from rest_framework import serializers
from .models import News,Youtube

# class DailyissueSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dailyissue
#         fields = '__all__'
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ('content','sort','start')

class NewsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        exclude = ('content','sort','start')

class YoutubeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = '__all__'