from django.shortcuts import render
import requests, json
from .models import Dailyissue
# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

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

    result = []
    k = 1
    for i in response['return_object']['topics']:
        result.append({'date':date,'category':category,'content':i['label']})
        k += 1
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii': False})
