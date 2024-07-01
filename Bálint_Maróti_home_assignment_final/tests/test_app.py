import requests



data = {"url": "https://www.examplle.com/", "shortcode": "111113"}

response = requests.post("http://localhost:8000/shorten", json=data)
print(response.json())
# Response: {'shortcode': 'asd223'}

# Running it again:
# data = {"url": "https://www.examle.com/", "shortcode": "asd223"}
#response = requests.post("http://localhost:8000/shorten", json=data)
#print(response.json())
# Response: {'error': 'The provided shortcode is already in use'}

# data = {"url": "https://www.examle.com/", "shortcode": "asd2133"}
# response = requests.post("http://localhost:8000/shorten", json=data)
# print(response.json())
# Response: {'error': 'The provided shortcode is invalid'}

# response = requests.get("http://localhost:8000/asd213")
# print(response.json())
# Response: {'location': 'https://www.examle.com/'}

# response = requests.get("http://localhost:8000/asd2133")
# print(response.json())
# Response: {'error': 'Shortcode not found'}



# response = requests.get("http://localhost:8000/asd223")
# print(response.json())
#Response: {'location': 'https://www.examle.com/'}
# 
# 
# response = requests.get("http://localhost:8000/asd223/stats")
# print(response.json())

