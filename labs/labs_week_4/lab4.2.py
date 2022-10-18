# This prog accesses Andrew's book API

import requests

url = "http://andreqbeatty1.pythonanywhere.com/books"
response = requests.get(url)
print(response.json())