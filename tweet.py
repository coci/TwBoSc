# -*- coding: utf-8 -*-
import tweepy
import sys
from cfg import consumer_key, consumer_secret, access_token, access_token_secret


reload(sys)
sys.setdefaultencoding('utf-8')

def tweeti(titlePost ,correctUrl):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	api.update_status('بچه ها پست جدید من :'+"\n" + titlePost +"\n"+ correctUrl)


