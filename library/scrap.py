# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from requests import get
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def sC():
	global titlePost
	global correctUrl
	url = 'http://www.thecoci.me/swift' # where you need to scrap from this ? insert link here

	response = get(url) #request to get url

	soup = BeautifulSoup(response.text,'lxml')

	titlePost = soup.find('a', {'itemprop': 'url'}).get_text()
	urlPost = soup.find('a', {'itemprop': 'url'})['href']
	correctUrl ="www.thecoci.me"+urlPost
	return titlePost
	return correctUrl
'''if need scrap all item
	for link in soup.find_all('a', {'itemprop': 'url'}):
    print(link['href'])
    print(link.get_text())
'''
'''
if you need crawl certain post use this : 
soup.find('a', {'itemprop': 'url'})[0].get_text()
zero can change for you
'''


