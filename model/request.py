import requests

url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':[2, 0, 1, -1, 2, 3, 3, -2, 3, 2, 0, 1, 3, -3, 0]})
print(r.json())