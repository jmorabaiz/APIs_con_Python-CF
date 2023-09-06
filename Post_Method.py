import requests

URL = 'https://httpbin.org/post'

# Query
# Cuerpo de petición
# Encabezado

headers = {
    'course': 'Curso de API con Python',
    'version': '2.0',
    'author': 'JMMB'
}

data = {
    'username': 'juan',
    'password': 'password123'
}

params = {
    'platform': 'CodigoFacilito'
}

response = requests.post(URL, data=data, headers=headers, params=params)

# if response.status_code == 200:
if response.status_code == requests.codes.ok:
    payload = response.json()
    print(payload)

    print(response.url)
