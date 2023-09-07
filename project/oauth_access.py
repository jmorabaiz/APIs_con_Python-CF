import requests
from settings import *

# Manually authorize to obtain value from the 'code'.
# https://github.com/login/oauth/authorize?client_id=58d333fd8c53d01a827c&scope=user

# After authorization use de code value: https://codigofacilito.com/?code=eac86c4573c961b33431

code = 'eac86c4573c961b33431'

URL = 'https://github.com/login/oauth/access_token'

params = {
    'client_id': CLIENT_ID,
    'client_secret': SECRET_ID,
    'code': code
}

headers = {
    'Accept': 'application/json'
}

response = requests.post(URL, params=params, headers=headers)

if response.status_code == 200:
    print(response.json())
