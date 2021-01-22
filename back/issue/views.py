from django.shortcuts import render
import requests, json
from urllib.parse import urlencode

# Create your views here.
def issuemaker():

    # URL 지정
    url = 'http://svc.saltlux.ai:31781'

    # Header 정보 지정
    headers = {'Content-Type': 'application/json; charset:utf-8'}

    # Request Parameter 정보 지정
    params ={
        'key': 'fc95de29-1c01-4271-b099-56ffb2e8144d',
        'serviceId': '11484686567',
        'argument': {
            "date": "2021-01-21",
            "category": "ENTERTAINMENT"
        }
    }

    response = json.loads(requests.post(url, headers=headers, data=json.dumps(params)).text)
    #-*-coding: utf-8
    # print(response)
    k = 1
    for i in response['return_object']['topics']:
        print(k,i['label'])
        k += 1

issuemaker()