import json
import requests
def keyword_mining(question):

    url = 'http://svc.saltlux.ai:31781'

    headers = {'Content-Type': 'application/json; charset:utf-8'}

    params ={
        'key': 'fc95de29-1c01-4271-b099-56ffb2e8144d',
        'serviceId': '00116013830',
        'argument': {
            "question": question,
        }
    }

    response = json.loads(requests.post(url, headers=headers, data=json.dumps(params)).text)

    result = []
    k = 0
    for i in response['return_object']['keylists']:
        result.append(i['keyword'])
        k += 1
        if k == 5:
            break
    return result
# print(keyword_mining('코로나 백신에 대한 나의 생각 안녕하세요 저는 코로나 뉴스를 보고 의견 작성해봅니다. 코로나는 현재 생활속에서 매우 많은 피해를 주고 있습니다. 영세업자는 물론이고 많은 국민들은 고통속에서 하루를 보내고 있습니다. 그놈의 백신이 빨리 보급될 수 있다면 현 상황이 해결될꺼라고 보시나요? 여러분들은 어떻게 생각하는지 궁금합니다!'))


def emotion(comment):
    url = 'http://svc.saltlux.ai:31781'

    headers = {'Content-Type': 'application/json; charset:utf-8'}

    params ={
        'key': 'fc95de29-1c01-4271-b099-56ffb2e8144d',
        'serviceId': '11987300804',
        'argument': {
                        "type": '1',
                        "query": comment
                    }
    }

    response = json.loads(requests.post(url, headers=headers, data=json.dumps(params)).text)
    return response['Result']
