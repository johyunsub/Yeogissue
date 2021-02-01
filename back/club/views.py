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

# 클럽 리스트 보기
@api_view(['GET'])
def club_list(request):
    club = Club.objects.all()
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
        print(user)
        club = Club.objects.get(title=request.data.get('title'))
        print(club)
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
    # user = MyUser.objects.get(id=request.data.get('user'))
    # print(user)
    user_id = request.data.get('user')
    # club_member = Club_member.objects.get(Q(club_id=club_pk)&Q(is_admin=True))
    # club_member_admin = club_member.user
    # print(club_member_admin)
    club_master = club.master

    if request.method == 'PUT':
        # if club_member_admin.id == user.id:
        if club_master == user_id:
            serializer = ClubUpdateSerializer(club, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'권한없음'})
        
    else:
        # if club_member_admin.id == user.id:
        if club_master == user_id:
            club.delete()
            return Response({ 'id': club_pk }, status=status.HTTP_204_NO_CONTENT)
        return Response({'권한없음'})
        
@api_view(['POST'])
def club_article(request):
    serializer = ClubArticleCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def club_article_detail(request, club_article_pk):
    
    club_article = get_object_or_404(Club_article, pk=club_article_pk)
    

    if request.method == 'GET':
        serializer = ClubArticleSerializer(club_article)
        return Response(serializer.data)


    # user = MyUser.objects.get(id=request.data.get('user'))
    user = request.data.get('user')
    if request.method == 'PUT':
        if club_article.user_id == user:
            serializer = ClubArticleUpdateSerializer(club_article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'권한없음'})

    else:
        if club_article.user_id == user:
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