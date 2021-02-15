from rest_framework import serializers
from .models import Alarm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        exclude = ['token']
        # fields = '__all__'

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','nickname','introduce_text','image']

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = '__all__'