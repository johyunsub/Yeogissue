from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArticleListSerializer, ArticleSerializer,HashtagSerializer,CommentSerializer, HashtagSerializer2,ReCommentSerializer
from .models import Article, Hashtag, Comment, ReComment

from .use_ai import keyword_mining, emotion

from accounts.models import MyUser as User
from accounts.models import Alarm

from django.db.models import Count

# 의견나눔 게시글
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all().order_by('-id')
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
        print(request.data.get('name'))
        # for i in list(map(str,request.data.get('name').split(','))):
        for i in request.data.get('name'):
            # print(i.strip(),'i')
            data['name']= i.strip()
            hashtag_create(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def hashtag_create(data):
    name = data['name']
    # print(name)
    if Hashtag.objects.filter(name=name).exists():
        hash = Hashtag.objects.get(name=name)
        hash.post_cnt += 1
        hash.articles.add(data['articles'][0])  
        hash.user.add(data['user'][0])
        hash.save()
        # 숫자세기
        # print(hash.articles.all().count())
    else:
        # print(name,'없음')
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

# 댓글 감정 분석
@api_view(['POST'])
def emotion_comment(request):
    emotion_co = emotion(request.data.get('content'))

    data = request.GET.copy()
    data['content'] = request.data.get('content')
    data['user'] = request.data.get('user')
    data['opinion_type'] = request.data.get('opinion_type')
    
    print(emotion_co)
    if emotion_co[0][0] > 0.5:
        data['emotion']= emotion_co[0][1]
    else:
        data['emotion'] = '감정불가'
    
    return Response(data)

# 의견나눔 게시글 댓글
@api_view(['POST'])
def create_comment(request, article_pk):
    
    # emotion = emotion_comment(request.data.get('content'))

    article = get_object_or_404(Article, pk=article_pk)
    print(request.data)
    if int(request.data.get('opinion_type')) == True:
        article.agree_count += 1
        article.save()
    elif int(request.data.get('opinion_type')) == False:
        article.disagree_count += 1
        article.save()

    # data = request.GET.copy()
    # print(data)
    # data['content'] = request.data.get('content')
    # data['user'] = request.data.get('user')
    # data['opinion_type'] = request.data.get('opinion_type')
    
    # if emotion[0][0] > 0.5:
    #     data['emotion']= emotion[0][1]
    # else:
    #     data['emotion'] = '감정불가'
        
   
    # print(data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        alarm = Alarm()
        alarm.message_type = '댓글'
        alarm.user_id = article.user.id
        alarm.object_id = article_pk
        alarm.object_content = article.title
        alarm.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all().order_by('-id')
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
        if comment.opinion_type == True:
            comment.article.agree_count -= 1
            comment.article.save()
        elif comment.opinion_type == False:
            comment.article.disagree_count -= 1
            comment.article.save()
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)

# 댓글 신고
@api_view(['GET'])
def badcomment(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.badcomment += 1
    comment.save()

# 의견나눔 게시글 대댓글
@api_view(['POST'])
def create_recomment(request, comment_pk):

    emotion = emotion_comment(request.data.get('content'))
    print(emotion)
    comment = get_object_or_404(Comment, pk=comment_pk)

    data = request.GET.copy()
    print(data)
    data['content'] = request.data.get('content')
    data['user'] = request.data.get('user')
    if emotion[0][0] > 0.5:
        data['emotion']= emotion[0][1]
    else:
        data['emotion'] = '감정불가'
    print(data)


    serializer = ReCommentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(comment=comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def recomment_list(request):
    recomments = ReComment.objects.all().order_by('-id')
    serializer = ReCommentSerializer(recomments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def recomment_detail_update_delete(request, recomment_pk):
    recomment = get_object_or_404(ReComment, pk=recomment_pk)
    if request.method == 'GET':
        serializer = ReCommentSerializer(recomment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReCommentSerializer(recomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        recomment.delete()
        return Response({ 'id': recomment_pk }, status=status.HTTP_204_NO_CONTENT)
    return Response({'success'})

# 대댓글 신고
@api_view(['GET'])
def badrecomment(request,recomment_pk):
    recomment = get_object_or_404(ReComment, pk=recomment_pk)
    recomment.badcomment += 1
    recomment.save()
    return Response({'success'})


# 좋아요_스크랩
@api_view(['POST'])
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    print(request)
    # user가 article을 좋아요 누른 전체유저에 존재하는지.
    if article.like_users.filter(pk=request.data.get('user')).exists():
        # 좋아요 취소
        article.like_users.remove(request.data.get('user'))
        return Response({'success', 'dislike'},status=status.HTTP_201_CREATED)
    else:
        # 좋아요
        article.like_users.add(request.data.get('user'))
        alarm = Alarm()
        alarm.message_type = '좋아요'
        alarm.user_id = article.user.id
        alarm.object_id = article_pk
        alarm.object_content = article.title
        alarm.save()
        return Response({'success', 'like'},status=status.HTTP_201_CREATED)


# 댓글 좋아요
@api_view(['POST'])
def like_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    # print('a')
    # user가 article을 좋아요 누른 전체유저에 존재하는지.
    if comment.like_users.filter(pk=request.data.get('user')).exists():
        # 좋아요 취소
        print('a')
        comment.like_users.remove(request.data.get('user'))
        return Response({'success', 'dislike'},status=status.HTTP_201_CREATED)
    else:
        # 좋아요
        comment.like_users.add(request.data.get('user'))
        alarm = Alarm()
        alarm.message_type = '댓글좋아요'
        alarm.user_id = comment.user.id
        alarm.object_id = comment_pk
        alarm.object_content = comment.content
        alarm.save()
        return Response({'success', 'like'},status=status.HTTP_201_CREATED)



@api_view(['POST'])
def scrap(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.scrap_users.filter(pk=request.data.get('user')).exists():
        article.scrap_users.remove(request.data.get('user'))
    else:
        article.scrap_users.add(request.data.get('user'))
    return Response({'success'},status=status.HTTP_201_CREATED)


#하나의 유저가 스크랩한 게시물 목록 출력
@api_view(['GET'])
def myscrap(request,user_pk):
    myuser = get_object_or_404(User, pk=user_pk)
    scrap_list = myuser.scrap_articles.all().order_by('-id')
    serializer = ArticleListSerializer(scrap_list, many=True) 
    # print(scrap_list)
    return Response(serializer.data)


@api_view(['GET'])
def club_article(request,club_pk):
    article = Article.objects.filter(club_pk=club_pk).order_by('-id')
    serializer = ArticleListSerializer(article, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def hashtag_suggest(request):
    title = request.data.get('title')
    content = request.data.get('content')
    comment = title + content
    suggest = keyword_mining(comment)
    info = {
        'keyword' : suggest 
    }
    return Response(info)


@api_view(['POST'])
def search_bar(request):
    name = request.data.get('name')
    if Hashtag.objects.filter(name=name).exists():
        hash = Hashtag.objects.get(name=name)
        
        articles = hash.articles.all().order_by('-id')
        # print(articles) 
        serializer = ArticleListSerializer(articles, many=True) 
        
        return Response(serializer.data)
    else:
        return Response({'없음'})

# 해시태그 랭킹
@api_view(['GET'])
def top_hashtag(request):
    top_hashtag = Hashtag.objects.all().order_by('-post_cnt')[:10]
    serializer = HashtagSerializer(top_hashtag, many=True)

    return Response(serializer.data)

# 댓글 랭킹
@api_view(['GET'])
def comment_rank(request):
    articles = Article.objects.all().annotate(num_comment=Count('comment')).order_by('-num_comment')[:5]
    # print(articles)
    serializer = ArticleListSerializer(articles,many=True)

    return Response(serializer.data)

# 좋아요 랭킹
@api_view(['GET'])
def like_rank(request):
    articles = Article.objects.all().annotate(num_like=Count('like_users')).order_by('-num_like')[:5]
    # print(articles)
    serializer = ArticleListSerializer(articles,many=True)

    return Response(serializer.data)

# 해시태그-> 게시물 -> 댓글 -> 감정 개수
@api_view(['POST'])
def hash_emotion(request):
    hash_tag = request.data.get('hashtag')
    hashtag = Hashtag.objects.get(name=hash_tag)
    articles = hashtag.articles.all()
    data = {'기쁨':0,'신뢰':0,'공포':0,'놀라움':0,'슬픔':0,'혐오':0,'분노':0,'기대':0}
    for article in articles:
        comments = article.comment_set.all()
        # print(comments)
        for comment in comments:
            # print(comment.emotion)
            if comment.emotion == '기쁨':
                data['기쁨'] += 1
            elif comment.emotion == '신뢰':
                data['신뢰'] += 1
            elif comment.emotion == '공포':
                data['공포'] += 1
            elif comment.emotion == '놀라움':
                data['놀라움'] += 1
            elif comment.emotion == '슬픔':
                data['슬픔'] += 1
            elif comment.emotion == '혐오':
                data['혐오'] += 1
            elif comment.emotion == '분노':
                data['분노'] += 1
            elif comment.emotion == '기대':
                data['기대'] += 1
    # print(data)
    
    return Response(data)
    
