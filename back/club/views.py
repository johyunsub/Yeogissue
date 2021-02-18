from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Club, Club_article, Club_member
from .serializers import ClubSerializer, ClubInfoSerializer, ClublistSerializer, ClubUpdateSerializer, ClubArticleCreateSerializer, ClubArticleSerializer, ClubArticleUpdateSerializer, ClubMemberSerializer
from django.conf import settings
from accounts.models import MyUser
from django.db.models import Q
import datetime
import requests
import urllib
from bs4 import BeautifulSoup
from accounts.models import Alarm


    
# 클럽 이미지 바꾸기
@api_view(['POST']) 
def club_image(request,club_pk):
    image = request.data.get('image')
    print(image)
    print(type(image))
    # user_id = request.data.get('user')
    # user_id = '1'
    club = Club.objects.get(id=club_pk)
    club.image = image
    club.save()
    return Response({'success'})

# 클럽 리스트 보기
@api_view(['GET'])
def club_list(request):
    club = Club.objects.all().order_by('-id')
    serializer = ClubInfoSerializer(club, many=True)
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

# 클럽 클릭시 클럽 페이지로 이동 클럽 수정 삭제


@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request, club_pk):
    # club 모델의 인스턴스 생성
    club = get_object_or_404(Club, pk=club_pk)
    # 접속하려는 유저의 인스턴스 모델 생성
    print(club_pk)

    if request.method == 'GET':
        # 방문횟수

        # if Club_member.objects.filter(Q(user_id=user_id)&Q(club_id=club_pk)).exists():
        #     member = Club_member.objects.get(Q(user_id=user_id)&Q(club_id=club_pk))
        #     if member.is_active == True:
        #         member.visit_cnt += 1
        #         member.save()
        serializer = ClubInfoSerializer(club)
        return Response(serializer.data)

    print(request.data.get('user'))
    user_id = int(request.data.get('user'))

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
            return Response({'id': club_pk}, status=status.HTTP_204_NO_CONTENT)
        return Response({'권한없음'})


@api_view(['GET'])
def club_article_list_news(request, club_pk):
    # club_article = Club_article.objects.filter(club_id=club_pk).exclude(category='Youtube').order_by('-id')
    club_article = Club_article.objects.filter(
        Q(club_id=club_pk) & Q(category='News')).order_by('-id')
    serializer = ClubArticleSerializer(club_article, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def club_article_list_youtube(request, club_pk):
    club_article = Club_article.objects.filter(
        Q(club_id=club_pk) & Q(category='Youtube')).order_by('-id')
    serializer = ClubArticleSerializer(club_article, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def club_article_list_etc(request, club_pk):
    club_article = Club_article.objects.filter(
        Q(club_id=club_pk) & Q(category='etc')).order_by('-id')
    serializer = ClubArticleSerializer(club_article, many=True)
    return Response(serializer.data)


# url 게시글 작성
@api_view(['POST'])
def club_article(request):
    serializer = ClubArticleCreateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

        article = Club_article.objects.get(id=serializer.data['id'])
        link = serializer.data['url']
        if 'https://' not in link:
            link = 'https://'+serializer.data['url']
        # print(link)

        # 네이버 블로그
        # print(1)
        if 'blog.naver.com' in link:
            html = urllib.request.urlopen(link)
            source = html.read()
            soup = BeautifulSoup(source, 'html.parser')
            src = soup.body.find('iframe')['src']
            src = src.replace('&directAccess=false', '')
            src = 'https://blog.naver.com' + src
            link = src
        # 네이버 뉴스
        # print(1)
        if 'news.naver.com' in link:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
            html = requests.get(link, headers=headers).text
            source = html
        # 이외
        else:
            # print(1)
            html = urllib.request.urlopen(link)
            source = html.read()

        print(1)
        soup = BeautifulSoup(source, 'html.parser')
        # data = {}
        if soup.find_all('meta', {'property': 'og:site_name'}):
            # data['site_name']= soup.find_all('meta',{'property' :'og:site_name'})[0].get('content')
            article.site_name = soup.find_all('meta', {'property': 'og:site_name'})[
                0].get('content')
        if soup.find_all('meta', {'property': 'og:title'}):
            # data['title']=soup.find_all('meta',{'property':'og:title'})[0].get('content')
            article.title = soup.find_all('meta', {'property': 'og:title'})[
                0].get('content')
        if soup.find_all('meta', {'property': 'og:description'}):
            # data['description']=soup.find_all('meta',{'property':'og:description'})[0].get('content')
            article.description = soup.find_all('meta', {'property': 'og:description'})[
                0].get('content')
        if soup.find_all('meta', {'property': 'og:image'}):
            # data['image']=soup.find_all('meta',{'property':'og:image'})[0].get('content')
            article.image = soup.find_all('meta', {'property': 'og:image'})[
                0].get('content')
        if soup.find_all('meta', {'property': 'og:video:url'}):
            # data['video']=soup.find_all('meta',{'property':'og:video:url'})[0].get('content')
            article.video = soup.find_all('meta', {'property': 'og:video:url'})[
                0].get('content')

        member = Club_member.objects.get(
            Q(user_id=request.data.get('user')) & Q(club_id=request.data.get('club')))
        member.article_cnt += 1
        member.save()
        article.save()

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
        serializer = ClubArticleUpdateSerializer(
            club_article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        club_article.delete()
        return Response({'id': club_article_pk}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def club_signup(request, club_pk):
    user_id = request.data.get('user')
    user = get_object_or_404(MyUser, pk=user_id)
    club = get_object_or_404(Club, pk=club_pk)

    if Club_member.objects.filter(Q(club_id=club_pk) & Q(user_id=user)).exists():
        return Response({'이미 가입'})

    club_member = Club_member()
    club_member.user = user
    club_member.club = club
    if request.data.get('comment'):
        club_member.comment = request.data.get('comment')
    if club.is_private == False:
        club_member.is_active = True
        club_member.is_admin = False
        club_member.save()
        
        return Response({'가입성공'})
    club_member.is_active = False
    club_member.is_admin = False
    club_member.save()

    alarm = Alarm()
    alarm.message_type = '클럽승인신청'
    alarm.user_id = Club.objects.get(id=club_pk).master.id
    alarm.object_id = club_pk
    alarm.object_content = Club.objects.get(id=club_pk).title
    alarm.save()

    return Response({'가입보류'})


@api_view(['POST'])
def member_approve(request, club_pk):
    member = request.data.get('member')
    print(member)
    club_member = Club_member.objects.get(
        Q(club_id=club_pk) & Q(user_id=member))
    if request.method == 'POST':
        club_member.is_active = True
        club_member.signdate = datetime.date.today()
        club_member.save()

        alarm = Alarm()
        alarm.message_type = '클럽승인완료'
        alarm.user_id = member
        alarm.object_id = club_pk
        alarm.object_content = Club.objects.get(id=club_pk).title
        alarm.save()

        return Response({'멤버승인됨'})


@api_view(['DELETE'])
def member_delete(request, club_pk, member_id):
    club_member = Club_member.objects.get(
        Q(club_id=club_pk) & Q(user_id=member_id))
    club_member.delete()
    return Response({'멤버삭제됨'})

# 클럽 맴버 확인 및 클럽 가입 승인 대기 확인


@api_view(['POST'])
def member_check(request, club_pk):
    if request.data.get('type') == '승인':
        club_member = Club_member.objects.filter(
            Q(club_id=club_pk) & Q(is_active=True))
        serializer = ClubMemberSerializer(club_member, many=True)
    else:
        club_member = Club_member.objects.filter(
            Q(club_id=club_pk) & Q(is_active=False))
        serializer = ClubMemberSerializer(club_member, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def club_member_delete(request, club_pk):
    user_id = request.data.get('user')

    if Club_member.objects.filter(Q(club_id=club_pk) & Q(user_id=user_id)).exists():
        club_member = Club_member.objects.get(
            Q(club_id=club_pk) & Q(user_id=user_id))
        club_member.delete()

        return Response({'탈퇴했음'})
    return Response({'그런사람 없음'})

# 내가 가입한 클럽
@api_view(['POST']) 
def myclub(request):
    user = request.data.get('user')
    clubs = Club_member.objects.filter(Q(user_id=user)&Q(is_active=True)).values('club_id')
    
    # print(clubs)
    data = {}
    j = 0
    for i in clubs:
        j += 1
        club_ = Club.objects.filter(id=i['club_id'])
        if j == 1:
            club = club_
        else:
            # print(club)
            # print(club_)
            club = club.union(club_)
    club.order_by('-id')
    serializer = ClubInfoSerializer(club, many=True)
    return Response(serializer.data)    
