import requests
from lxml import etree

url = 'https://www.x23us.com/html/60/60948/24774656.html'

response = requests.get(url=url)
# print(response.text.encode())
