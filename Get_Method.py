import requests

# URL = 'https://httpbin.org/get?name=Eduardo&password=123&email=eduardo@codigofacilito.com'
URL = 'https://httpbin.org/get'

params = {
    'nombre': 'Eduardo Ismael',
    'password': '123',
    'email': 'eduardo@codigofacilito.com'
}
# query: ?name=Eduardo&password=123&email=eduardo@codigofacilito.com

response = requests.get(URL, params=params)  # GET

# print(response)
# print(response.status_code)
# print(type(response.text))  # str no es json
# print(response.json())  # Genera el json
# print(response.json())  # Genera el json
#
# payload = response.json()
#
# print('origin:', payload.get('origin'))
#
# print('url:', response.url)

if response.status_code == 200:
    payload = response.json()
    params = payload['args']
    print(params)
    print(response.url)
