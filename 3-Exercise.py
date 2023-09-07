import requests

URL = 'https://randomuser.me/api/'

count = int(input('Ingrese la cantidad de usuarios: '))

params = {'results': count}

response = requests.get(URL, params=params)

if response.status_code == 200:
    payload = response.json()
    results = payload.get('results')

    for user in results:
        name = user.get('name')
        print("{title} {first} {last}".format(**name))
