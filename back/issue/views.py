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
    category = request.data.get('category')
    # if Dailyissue.objects.filter(Q(date=date) & Q(category=category)).exists():
    #     data = Dailyissue.objects.filter(Q(date=date) & Q(category=category))
    #     return Response(json(data))
    # else:
        
        
        # # URL 지정
        # url = 'http://svc.saltlux.ai:31781'

        # # Header 정보 지정
        # headers = {'Content-Type': 'application/json; charset:utf-8'}

        # # Request Parameter 정보 지정
        # params ={
        #     'key': 'fc95de29-1c01-4271-b099-56ffb2e8144d',
        #     'serviceId': '11484686567',
        #     'argument': {
        #         "date": date,
        #         "category": category
        #     }
        # }

        # response = json.loads(requests.post(url, headers=headers, data=json.dumps(params)).text)
        # #-*-coding: utf-8
        # # print(response)
        # k = 1
        # for i in response['return_object']['topics']:
        #     print(k,i['label'])
        #     data = Dailyissue()
        #     data.date = date
        #     data.category = category
        #     data.content = i['label']
        #     data.save()
        #     k += 1
        # result = Dailyissue.objects.filter(Q(date=date) & Q(category=category))
        # return Response(result)

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
    print(response)
    result = []
    k = 1
    for i in response['return_object']['topics']:
        result.append({'date':date,'category':category,'content':i['label']})
        k += 1
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii': False})


import re

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   cleanrn = re.compile('&.*;')
   cleantext = re.sub(cleanrn, '', cleantext)
   return cleantext

def naver_search(issue):
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
        'query': issue
    }
    
    r = requests.get(url, params=query, headers=url_maker.header)
    # print(r,'rrrr')
    Info_dict = r.json()  
    # print(Info_dict,'확인')
    news_list = []
    for i in Info_dict['items']:
        title = remove_tag(i['title'])
        news_list.append({'title':title,
        'link':i['originallink'],
        })
    # print(news_list)
    # # link = news_list[1]['link']
    # link = 'https://gooweon.tistory.com/47'
    # print(link)
    # html = urllib.request.urlopen(link)
    # source = html.read()
    # soup = BeautifulSoup(source,'html.parser')
    # print(soup)

        # print('확인')
    
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
    data = []
    for i in response_dict['items']:
        news = {}
        news['title']=i['snippet']['title']
        news['videoId']='http://youtube.com/watch?v='+i['id']['videoId']
        data.append(news)
   
    return data

@api_view(['POST'])
def issue_search(request):
    issue = request.data.get('issue')
    info = {}
    news = naver_search(issue)
    youtube_info = youtube(issue)
    info['news'] = news
    info['youtube'] = youtube_info
    return JsonResponse(info,safe=False,json_dumps_params={'ensure_ascii': False})
