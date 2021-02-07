from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Club, Club_article, Club_member
from .serializers import ClubSerializer, ClublistSerializer,ClubUpdateSerializer,ClubArticleCreateSerializer,ClubArticleSerializer,ClubArticleUpdateSerializer
from django.conf import settings
from accounts.models import MyUser
from django.db.models import Q

import requests
import urllib
from bs4 import BeautifulSoup

# 클럽 리스트 보기
@api_view(['GET'])
def club_list(request):
    club = Club.objects.all().order_by('-id')
    serializer = ClublistSerializer(club,many=True)
    return Response(serializer.data)


# 클럽 생성하기
# 클럽 마스터한테 권한주기
@api_view(['POST'])
def club_create(request):
    serializer = ClubSerializer(data=request.data)
    # 클럽 이름 중복 시
    if Club.objects.filter(title=request.data.get('title')).exists():
        return Response({'중복되는 이름입니다.'})

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        user = MyUser.objects.get(id=request.data.get('master'))
        # print(user)
        club = Club.objects.get(title=request.data.get('title'))
        # print(club)
        club_member = Club_member()
        club_member.user = user
        club_member.club = club
        club_member.is_active = True
        club_member.is_admin = True
        club_member.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#클럽 클릭시 클럽 페이지로 이동 클럽 수정 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request, club_pk):
    # club 모델의 인스턴스 생성
    club = get_object_or_404(Club, pk=club_pk)
    
    
    if request.method == 'GET':
        serializer = ClubSerializer(club)
        return Response(serializer.data)

    # 접속하려는 유저의 인스턴스 모델 생성
   
    user_id = request.data.get('user')
   
    club_master = club.master.id
    # print(club_master==user_id)
    if request.method == 'PUT':
  
        if club_master == int(user_id):
            print('ddd')
            serializer = ClubUpdateSerializer(club, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'권한없음'})
        
    else:
    
        if club_master == int(user_id):
            club.delete()
            return Response({ 'id': club_pk }, status=status.HTTP_204_NO_CONTENT)
        return Response({'권한없음'})
        

@api_view(['GET'])
def club_article_list(request,club_pk):
    club_article = Club_article.objects.filter(club_id=club_pk).order_by('-id')
    serializer = ClubArticleSerializer(club_article,many=True)

    data_list = []
    for i in serializer.data:
        link = i['url']
        
        # 네이버 블로그
        if 'blog.naver.com' in link:
            html = urllib.request.urlopen(link)         
            source = html.read()
            soup = BeautifulSoup(source,'html.parser') 
            src = soup.body.find('iframe')['src']
            src = src.replace('&directAccess=false','')
            src = 'https://blog.naver.com' + src
            link = src
        # 네이버 뉴스
        if 'news.naver.com' in link:
            headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }
            html = requests.get(link,headers=headers).text
            source = html
        # 이외
        else:
            html = urllib.request.urlopen(link)
            source = html.read()
        
        soup = BeautifulSoup(source,'html.parser')
        data = {}
        if soup.find_all('meta',{'property' :'og:site_name'}):
            data['site_name']= soup.find_all('meta',{'property' :'og:site_name'})[0].get('content')
        if soup.find_all('meta',{'property':'og:title'}):
            data['title']=soup.find_all('meta',{'property':'og:title'})[0].get('content')
        if soup.find_all('meta',{'property':'og:description'}):
            data['description']=soup.find_all('meta',{'property':'og:description'})[0].get('content')
        if soup.find_all('meta',{'property':'og:image'}):
            data['image']=soup.find_all('meta',{'property':'og:image'})[0].get('content')
        if soup.find_all('meta',{'property':'og:video:url'}):
            data['video']=soup.find_all('meta',{'property':'og:video:url'})[0].get('content')
        
        data['id'] = i['id']
        data['category'] = i['category']
        data['comment'] = i['comment']
        data['created_at'] = i['created_at']
        data['updated_at'] = i['updated_at']
        data['user'] = i['user']
        data['club'] = i['club']
       
        data_list.append(data)

    send_data={}
    send_data['data']=data_list
    return Response(send_data)

@api_view(['POST'])
def club_article(request):
    serializer = ClubArticleCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'작성실패'})

@api_view(['GET', 'PUT', 'DELETE'])
def club_article_detail(request, club_article_pk):
    
    club_article = get_object_or_404(Club_article, pk=club_article_pk)
    

    if request.method == 'GET':
        serializer = ClubArticleSerializer(club_article)
        return Response(serializer.data)

    user = request.data.get('user')
    if request.method == 'PUT':
        if club_article.user_id == int(user):
            serializer = ClubArticleUpdateSerializer(club_article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'권한없음'})

    else:
        if club_article.user_id == int(user):
            club_article.delete()
            return Response({ 'id': club_article_pk }, status=status.HTTP_204_NO_CONTENT)
        return Response({'권한없음'})



@api_view(['POST'])
def club_signup(request,club_pk):
    user_id = request.data.get('user')
    user = get_object_or_404(MyUser,pk=user_id)
    club = get_object_or_404(Club,pk=club_pk)

    if Club_member.objects.filter(Q(club_id=club_pk)&Q(user_id=user)).exists():
        return Response({'이미 가입'})
    

    club_member = Club_member()
    club_member.user = user
    club_member.club = club
    club_member.is_active = True
    club_member.is_admin = False
    club_member.save()

    return Response({'승인되었습니다.'})


@api_view(['POST'])
def club_member_delete(request,club_pk):
    user_id = request.data.get('user')
    
    if Club_member.objects.filter(Q(club_id=club_pk)&Q(user_id=user_id)).exists():
        club_member = Club_member.objects.get(Q(club_id=club_pk)&Q(user_id=user_id))
        club_member.delete()

        return Response({'탈퇴했음'})
    return Response({'그런사람 없음'})