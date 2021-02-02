from rest_framework import serializers
# from .models import MyUser as User
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
        fields = ['id','email','nickname']