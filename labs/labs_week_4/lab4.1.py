# This prog shows how to access an API

import requests

url = "http://google.com"
response = requests.get(url)

print(response.text)