import requests
from settings import TOKEN

URL = 'https://api.github.com/user'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {TOKEN}'
}

# 1. Crear una aplicación de GitHub para obtener el client_id y el client_secret
# 2. Obtenemos el código del usuario → GET https://github.com/login/oauth/authorize?client_id=<client_id>&scope=user
# 3. Obtenemos el Access Token → POST https://github.com/login/oauth/access_token con parámetros de client_id, client_secret y code
# 4. Obtenemos datos del usuario que aceptó nuestra aplicación → GET https://api.github.com/user

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    username = response.json().get('login')
    print(username)
