import pyshorteners
import requests
url = input("Long url: ")
ACCESS_TOKEN = '573af123b83ba7d0aa4901bfb0643c46e70c1e8e'
shortener = pyshorteners.Shortener(api_key=ACCESS_TOKEN)
print(shortener.bitly.short(url))
headers = {
    'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
    'Content-Type': 'application/json',}
data = { "long_url": url}
response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
print(response.json()['link'])