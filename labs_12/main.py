import requests
import json

url = 'https://github.com/solovey-88'


def make_request(method, url, data=None):
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, data=data)
    elif method == 'OPTIONS':
        response = requests.options(url)

    print(f'Запрос {method} {url} выполнен.')
    if data:
        print(f'Тело запроса: {data}')

    print(f'Код ответа: {response.status_code}')
    print(f'Заголовки ответа: {response.headers}')
    print(f'Тело ответа: {response.text}\n')


make_request('OPTIONS', url)
make_request('GET', url)
make_request('POST', url, data=json.dumps({'key': 'value'}))
