#!/usr/local/bin/python3

from tweepy import streaming, OAuthHandler, StreamListener, Stream
from pymongo import MongoClient
import json
import cgi
import urllib
import urllib.request
import pymongo
from html.parser import HTMLParser

#consumer key, secret and access secret and token

ckey = "NmkkUBSfunillGDcQVsTC2yKS"
csecret = "RA8plLhgCqvXzuLdVgjpiyDxzWrQidxqb8H7stfJRY8wQA9VLN"
atoken = "805122203389825025-s2VJfsXaCDw784H5fhooqNM2tgqRnUL"
asecret = "wtK57HGCKx8tFvFZLMHNmasGUcwmb6SAAT2LQmE2Kg9v4"

client = MongoClient()
db = client.Twitterdb
collection = db.tweets
posts = db.posts

#a rough bounding box of USA, Hawaii, and Alaska
UNITED_STATES = [-125.9,24.1,-66.3,49.3]
HAWAII = [-161.03,18.27,-154.06,22.86]
ALASKA = [-168.09,52.02,-140.8,71.76]

class listener(StreamListener):
	def on_data(self, data):
		tweet = json.loads(HTMLParser().unescape(data))
		#post_id = posts.insert_one(tweet).inserted_id
		#print(tweet)

		with open('data.json', 'a') as outfile:
			json.dump(tweet, outfile)
		with open('data.json', 'a') as outfile:
			("/n")





	def on_error(self, status_code):
		 print >> sys.stderr, 'Encountered error with status code:', status_code
		 return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream


#Necessary authentication from twitter app to use API
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(locations= UNITED_STATES+HAWAII+ALASKA) #filters within bound box of USA, including Hawaii and Alaska
