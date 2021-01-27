from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article, Hashtag
# Create your views here.


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        #2. 모델에서 가져온 데이터를 Serializing한다.
        serializer = ArticleSerializer(article)
        #3. 응답 해준다.
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