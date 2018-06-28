# -*- coding: utf-8 -*-
import tweepy
from bs4 import BeautifulSoup
from requests import get
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


url = 'http://www.thecoci.me/swift' # where you need to scrap from this ? insert link here

response = get(url) #request to get url

soup = BeautifulSoup(response.text,'lxml')

titlePost = soup.find('a', {'itemprop': 'url'}).get_text()
urlPost = soup.find('a', {'itemprop': 'url'})['href']
correctUrl ="www.thecoci.me"+urlPost
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
from cfg import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status('بچه ها پست جدید من :'+"\n" + titlePost +"\n"+ correctUrl)


