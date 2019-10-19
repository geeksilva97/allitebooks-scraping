import requests
import re
from bs4 import BeautifulSoup

URL = 'http://www.allitebooks.org/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

main = soup.find('main', {'id': 'main-content'})
pagination = main.find('div', {'class': 'pagination'}).find('span', {'class': 'pages'}).text

pages = pagination.split('/')
first,last = map(lambda page: int(re.sub('\D', '', page), pages))

print(first)
print(last)