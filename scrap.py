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



