from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArticleListSerializer, ArticleSerializer,HashtagSerializer,CommentSerializer, HashtagSerializer2
from .models import Article, Hashtag, Comment
# Create your views here.

# 의견나눔 게시글
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)      
    return Response(serializer.data)

@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = {}
        data['articles']=[serializer.data['id']]
        data['user']=[request.data.get('user')]
        print(list(map(str,request.data.get('name').split(','))))
        for i in list(map(str,request.data.get('name').split(','))):
            print(i.strip(),'i')
            data['name']= i.strip()
            hashtag_create(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def hashtag_create(data):
    name = data['name']
    print(name)
    if Hashtag.objects.filter(name=name).exists():
        hash = Hashtag.objects.get(name=name)
        hash.articles.set(data['articles'])  
        hash.user.set(data['user'])
        hash.save()
        # print(hash.articles)
    else:
        print(name,'없음')
        serializer = HashtagSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        article.read_count += 1
        article.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # print(request.data)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        article.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


# 의견나눔 게시글 댓글
@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    print('a')
    # user가 article을 좋아요 누른 전체유저에 존재하는지.
    if article.like_users.filter(pk=request.data.get('user')).exists():
        # 좋아요 취소
        print('a')
        article.like_users.remove(request.data.get('user'))
    else:
        # 좋아요
        article.like_users.add(request.data.get('user'))
    return Response({'success'},status=status.HTTP_201_CREATED)

@api_view(['POST'])
def scrap(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.scrap_users.filter(pk=request.data.get('user')).exists():
        article.scrap_users.remove(request.data.get('user'))
    else:
        article.scrap_users.add(request.data.get('user'))
    return Response({'success'},status=status.HTTP_201_CREATED)