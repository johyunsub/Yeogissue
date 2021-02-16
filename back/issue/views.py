from django.shortcuts import render
import requests, json
from .models import Dailyissue,News, Youtube
# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import urllib
from bs4 import BeautifulSoup
from .serializers import NewsSerializer,NewsSerializer2, YoutubeSerializer, YoutubeSerializer2
import requests

@api_view(['POST'])
def issuemaker(request):
    date = request.data.get('date')
    # category_list = ['ENTERTAINMENT','IT_SCIENCE','WORLD','ECONOMY','SPORTS','POLITICS','SOCIETY/LIVING']
    category = request.data.get('category')
    url = 'http://svc.saltlux.ai:31781'

    headers = {'Content-Type': 'application/json; charset:utf-8'}

    params ={
        'key': 'fc95de29-1c01-4271-b099-56ffb2e8144d',
        'serviceId': '11484686567',
        'argument': {
            "date": date,
            "category": category
        }
    }

    response = json.loads(requests.post(url, headers=headers, data=json.dumps(params)).text)
    # print(response)
    result = []
    k = 1
    for i in response['return_object']['topics']:
        if i['label']:
            result.append({'date':date,'category':category,'content':i['label']})
            k += 1
            if k==11 : break
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii': False})


import re

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   cleanrn = re.compile('&.*;')
   cleantext = re.sub(cleanrn, '', cleantext)
   return cleantext

def naver_search(issue,start,sort):
    print('없ㅇ므')
    class NaverNewsURLMaker:
        url = 'https://openapi.naver.com/v1/search'
        header = {
            'X-Naver-Client-Id': 'KoDu00KTEpd323frWLQa',   
            'X-Naver-Client-Secret': 'eN2R3foM2a'   
        }
        def get_url(self, category):
            return f'{self.url}/{category}.json?'
    url_maker = NaverNewsURLMaker()
    url = url_maker.get_url('news')

    query = {    
        'query': issue,
        'start': start,
        'sort' : sort
    }
    
    r = requests.get(url, params=query, headers=url_maker.header)
    Info_dict = r.json()
    # print(Info_dict,'확인')
    news_list = []
    news_list.append({'total':Info_dict['total']})
    for i in Info_dict['items']:
        # link = i['originallink']
        link = i['link']
        # print(link)
        if 'news.naver.com' in link:
            headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }
            html = requests.get(link,headers=headers).text
            source = html
        # 이외
        else:
            html = urllib.request.urlopen(link)
            source = html.read()
        
        soup = BeautifulSoup(source,'html.parser')
        # print(soup.find_all('meta'))
        data = {}
        data['link']=link
        if soup.find_all('meta',{'name' :'twitter:creator'}):
            # print(soup.find_all('meta',{'name' :'twitter:creator'}))
            data['site_name']= soup.find_all('meta',{'name' :'twitter:creator'})[0].get('content')[:50]
        if soup.find_all('meta',{'property':'og:title'}):
            data['title']=soup.find_all('meta',{'property':'og:title'})[0].get('content')[:50]
        if soup.find_all('meta',{'property':'og:description'}):
            data['description']=soup.find_all('meta',{'property':'og:description'})[0].get('content')[:300]
        if soup.find_all('meta',{'property':'og:image'}):
            data['image']=soup.find_all('meta',{'property':'og:image'})[0].get('content')[:150]
        # if soup.find_all('meta',{'property':'og:video:url'}):
        #     data['video']=soup.find_all('meta',{'property':'og:video:url'})[0].get('content')
        
        news_list.append(data)
        data['content'] = issue
        data['sort'] = sort
        data['start'] = start
        serializer = NewsSerializer2(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
                                                                
        # print(news_list)

    return news_list


# 유튜브
def youtube(issue,order,token):
    print('없ㅇ므')

    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': 'AIzaSyB7GhJqvpHemgECyjSuGQfdsgcizl_Tb90',
        'part': 'snippet',
        'type': 'video',
        'maxResults': '30',
        'q': issue,
    # order = ['relevance','date']
        'order':order,
        'pageToken': token,
    }
    response = requests.get(url, params)
   
    response_dict = response.json()
    # print(response_dict)

    # data = []
    # if response_dict.get('pageInfo'):
    #     data.append({'total':response_dict['pageInfo']['totalResults']})
    # if response_dict.get('prevPageToken'):
    #     data[0]['prevToken']=response_dict['prevPageToken']
    # if response_dict.get('nextPageToken'):
    #     data[0]['nextToken']=response_dict['nextPageToken']
    # print(response_dict)
    j=0
    for i in response_dict['items']:
        news = {}
        news['title']=i['snippet']['title'][:50]
        news['description']=i['snippet']['description'][:150]
        news['thumbnails']=i['snippet']['thumbnails']['medium']['url']
        news['channelTitle']=i['snippet']['channelTitle'][:50]
        news['publishTime']=i['snippet']['publishTime'][:50]
        news['videoId']='http://youtube.com/watch?v='+i['id']['videoId']
        # data.append(news)
        news['content'] = issue
        news['sort'] = order
        news['start'] = (j//10)*10 + 1
        j += 1
        # print(news)
        serializer = YoutubeSerializer2(data=news)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    youtubes = Youtube.objects.filter(Q(content=issue)&Q(sort=order)&Q(start='1'))
    return youtubes

# 뉴스
@api_view(['POST'])
def issue_news(request):
    issue = request.data.get('content')
    start = request.data.get('start')
    sort = request.data.get('sort')
    news = Youtube.objects.all()
    news.delete()
    
    if News.objects.filter(Q(content=issue)&Q(sort=sort)&Q(start=start)).exists():
        print('잇음')
        news_data = News.objects.filter(Q(content=issue)&Q(sort=sort)&Q(start=start))
        serializer = NewsSerializer(news_data, many=True)
        return Response({'news':serializer.data})
    info = {}
    news = naver_search(issue,start,sort)
    info['news'] = news
    return JsonResponse(info,safe=False,json_dumps_params={'ensure_ascii': False})

# 유튜브
@api_view(['POST'])
def issue_youtube(request):

    issue = request.data.get('content')
    order = request.data.get('order')
    start = request.data.get('start')
    token = ''
    # news = Youtube.objects.all()
    # news.delete()
    # if request.data.get('token'):
    #     token = request.data.get('token')
    if Youtube.objects.filter(Q(content=issue)&Q(sort=order)&Q(start=start)).exists():
        print('잇음')
        youtube_data = Youtube.objects.filter(Q(content=issue)&Q(sort=order)&Q(start=start))
        serializer = YoutubeSerializer(youtube_data, many=True)
        return Response({'youtube':serializer.data})

    info = {}

    youtube_info = youtube(issue,order,token)
    serializer = YoutubeSerializer(youtube_info,many=True)
    return Response({'youtube':serializer.data})
    # info['youtube'] = youtube_info

    # return JsonResponse(info,safe=False,json_dumps_params={'ensure_ascii': False})
