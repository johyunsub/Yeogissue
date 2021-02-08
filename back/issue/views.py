from django.shortcuts import render
import requests, json
from .models import Dailyissue
# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import urllib
from bs4 import BeautifulSoup


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
    news_list.append(Info_dict['total'])
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

        news_list.append(data)
        # print(news_list)

    return news_list

import requests
def youtube(issue):
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': 'AIzaSyCUK-7ji58muTsxvtW6TfFwNy4fWgbzkjY',
        'part': 'snippet',
        'type': 'video',
        'maxResults': '10',
        'q': issue,
    }
    response = requests.get(url, params)
   
    response_dict = response.json()
    # print(response_dict)

    data = []
    data.append(response_dict['pageInfo']['totalResults'])
    for i in response_dict['items']:
        news = {}
        news['title']=i['snippet']['title']
        news['description']=i['snippet']['description']
        news['thumbnails']=i['snippet']['thumbnails']['default']
        news['channelTitle']=i['snippet']['channelTitle']
        news['videoId']='http://youtube.com/watch?v='+i['id']['videoId']
        data.append(news)
   
    return data

@api_view(['POST'])
def issue_search(request):
    issue = request.data.get('issue')
    start = request.data.get('start')
    sort = request.data.get('sort')
    info = {}
    news = naver_search(issue,start,sort)
    youtube_info = youtube(issue)
    info['news'] = news
    info['youtube'] = youtube_info
    return JsonResponse(info,safe=False,json_dumps_params={'ensure_ascii': False})
