from rest_framework import serializers
from .models import News
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