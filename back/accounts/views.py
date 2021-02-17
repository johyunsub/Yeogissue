from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,GetUserSerializer, AlarmSerializer
from .models import MyUser as User
from .models import Alarm
from django.core.mail import EmailMessage
from .tokens import make_code
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework_jwt.views import obtain_jwt_token

from django.contrib.auth.hashers import check_password

from django.db.models import Q


@api_view(['POST'])
def make_admin(request):
    email = request.data.get('email')
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        user.is_admin = True
        user.is_active = True
        user.save()
        return Response({'success'})
    return Response({'fail'})

# Create your views here.
@api_view(['POST'])
def nickname_check(request):
    nickname = request.data.get('nickname')
    # print(nickname)
    if nickname == None or User.objects.filter(nickname=nickname).exists():
        # print(nickname)
        return Response({'fail'})
    
    return Response({'success'})

@api_view(['POST'])
def userid_check(request):
    email = request.data.get('email')
    # print(email)
    
    if email == None or User.objects.filter(email=email).exists():
        return Response({'fail'})
    
    return Response({'success'})

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # user.is_active = True
        user.set_password(request.data.get('password'))
        token = make_code()
        user.token = token
        user.image = 'images/profile.jpg'
        user.save()
        print(token)
        message = f'이메일 인증을 위해서 {token} 을 입력해주세요'
        mail_title = '여기이슈 이메일 인증메일입니다.'
        mail_to = request.data.get('email')
        email = EmailMessage(mail_title,message,to=[mail_to])
        email.send()
        print(type(serializer.data))
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def email_check(request):
    if User.objects.filter(email=request.data.get('email')).exists():
        user = User.objects.get(email=request.data.get('email'))
    else:
        return Response({'등록된 이메일이 없음'})
    token = request.data.get('token')
    if user.token == token:
        user.is_active = True
        user.save()
        return Response({'success'})
    return Response({'fail'})

@api_view(['POST'])
def user_delete(request):
    email = request.data.get('email')
    print(email)
    if User.objects.filter(email=email).exists():
        User.delete(User.objects.get(email=email))
        return Response({'success'})
    
    return Response({'fail'})

import base64
import os
from datetime import datetime

@api_view(['POST'])
def user_update(request):
    email = request.data.get('email')
    # password = request.data.get('password')
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        if request.data.get('nickname'):
            nickname = request.data.get('nickname')
            user.nickname = nickname
        if request.data.get('introduce'):
            introduce = request.data.get('introduce')
            user.introduce_text = introduce
        # if request.data.get('images'):
        #     image = request.data.get('images')
        #     print(image,'123132123312 ')
            
        #     user.image = image
        user.save()
        return Response({'success'})
    return Response({'없는계정'})


@api_view(['POST'])
def get_user(request):
    user = get_object_or_404(get_user_model(), email=request.data.get('email'))
    serializer = GetUserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def get_user_id(request):
    user = get_object_or_404(get_user_model(), id=request.data.get('id'))
    serializer = GetUserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        if user.is_active == False:
            return Response({'0'})
    return Response({'1'})


@api_view(['POST'])
def passwordChange(request):
    email = request.data.get('email') 
    PW = request.data.get('currentPW')
    newPW = request.data.get('newPW')
    newPW2 = request.data.get('newPW2')

    user = User.objects.get(email=email)
    
    if check_password(PW,user.password):
        if newPW == newPW2:
            user.set_password(newPW)
            user.save()
            return Response({'0'}) #성공
        else:
            return Response({'1'}) #비밀번호불일치
    else:
        return Response({'2'}) #현재비번 틀림

@api_view(['POST'])
def sendPassword(request):
    email = request.data.get('email')
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        token = make_code()
        print(token)
        # user.token = token
        user.set_password(token)
        user.save()
        message = f'임시비밀번호는 {token} 입니다.'
        mail_title = '여기이슈 임시비밀번호 메일입니다.'
        mail_to = request.data.get('email')
        email = EmailMessage(mail_title,message,to=[mail_to])
        email.send()
        return Response({'0'})
    return Response({'없음'})
    
@api_view(['POST']) 
def alarm(request):
    user_id = request.data.get('user')
    alarm = Alarm.objects.filter(Q(user_id=user_id)&Q(check=False)).order_by('-id')
    serializer = AlarmSerializer(alarm, many=True)
    return Response(serializer.data)

@api_view(['POST']) 
def alarm_total(request):
    user_id = request.data.get('user')
    alarm = Alarm.objects.filter(user_id=user_id).order_by('-id')
    serializer = AlarmSerializer(alarm, many=True)
    return Response(serializer.data)

@api_view(['POST']) 
def alarm_check(request):
    alarm_id = request.data.get('alarm_id')
    alarm = Alarm.objects.get(id=alarm_id)
    alarm.check = True
    alarm.save()
    return Response({'success'})


@api_view(['POST']) 
def profile_image(request,user_id):
    image = request.data.get('image')
    print(image)
    print(type(image))
    print(user_id)    
    user = User.objects.get(id=user_id)
    user.image = image
    user.save()
    return Response({'success'})
    
