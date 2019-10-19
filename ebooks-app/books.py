"""
Módulo que lista os livros buscados na página inicial

	books (list) - lista de livros buscados
"""

import requests
from bs4 import BeautifulSoup
import json

books = []

def list_books_page(URL = 'http://www.allitebooks.org/'):
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	main = soup.find('main', {'id': 'main-content'})
	articles = main.find_all('article')

	for article in articles:
		#thumb information
		entry_thumbnail = article.find('div', {'class': 'entry-thumbnail'})
		image_src = entry_thumbnail.find('img')['src']

		# body
		entry_body = article.find('div', {'class': 'entry-body'})
		a = entry_body.find('header').find('h2').a

		title = a.text
		url = a['href']

		# metadata
		entry_meta = article.find('div', {'class': 'entry-meta'})
		a = entry_meta.find('h5', {'class': 'entry-author'}).a
		author_name = a.text
		author_url = a['href']

		summary = article.find('div', {'class': 'entry-summary'}).find('p').text

		books.append({
			'thumbnail': image_src,
			'title': title,
			'url': url,
			'summary': summary,
			'author': {
				'name': author_name,
				'url': author_url
			}
		})

	# print(json.dumps(books))


		
