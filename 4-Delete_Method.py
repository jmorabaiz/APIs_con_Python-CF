import requests

# GET = get
# POST = post
# PUT = pu
# DELETE = delete

URL = 'https://httpbin.org/delete'
response = requests.delete(URL,
                        params={'name': 'Juan'},
                        headers={'version': '2.0'},
                        data={'id': 1})

if response.status_code == 200:
    print(response.text)
