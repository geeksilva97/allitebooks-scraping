"""
Módulo que lista as categorias

	categories (list) - lista de categorias buscadas
"""

import requests
from bs4 import BeautifulSoup
import json

URL = 'http://www.allitebooks.org/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

ul = soup.find('ul', {'id': 'menu-categories'})
items = ul.find_all('li')

categories = []

for li in items:
	a = li.a
	categories.append({ 'url': a['href'], 'name': a.text })

# print(json.dumps(categories))
