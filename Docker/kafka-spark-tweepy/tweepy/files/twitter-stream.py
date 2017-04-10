#!/usr/bin/python
#got tips and some help from CU's 3308, team Vision Dev team, in repos I have contributed to
#got tips from
#http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from HTMLParser import HTMLParser
import time
import random
import sys



#consumer key, secret and access secret and token
#found on dev.twitter.com
ckey = "RVsESV3A0hCi5wBiZmV5bJRn3"
csecret = "z8VcD5P1JMnPuC61sslnMYgtRNg4err2nZX3YTsPgMogeGYV8V"
atoken = "828689526373560320-7GDNGOMNpCFVJdGOCf7swCxLc4lB585"
asecret = "FKtjnr2MV7HtUxNjboBgHJrn27OZGUFaguHWYKRG6uLqR"

#a rough bounding box of USA, Hawaii, and Alaska
UNITED_STATES = [-125.9,24.1,-66.3,49.3]
HAWAII = [-161.03,18.27,-154.06,22.86]
ALASKA = [-168.09,52.02,-140.8,71.76]
dict ={
		'Jan' : '01',	#dict is used to convert month abv. numerical month
        'Feb' : '02',
        'Mar' : '03',
        'Apr' : '04',
        'May' : '05',
        'Jun' : '06',
        'Jul' : '07',
        'Aug' : '08',
        'Sep' : '09',
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
}

class listener(StreamListener):



	def on_data(self, data):

		tweet = json.loads(HTMLParser().unescape(data))
		try:
			hashtags = str([hashtag['text'] for hashtag in tweet['entities']['hashtags']])

#			coordinates is NULL if disabled. An if statement is needed to use the data when available
			if tweet['coordinates']:

				#random.randint(1, 100)
				#if(random.randint > 99):   #optional for terminate based off of probability set up by user
				#	print "terminated"
				#	return False
				geo_location = str(tweet['coordinates']['coordinates'])
				geo_location_long = geo_location.split("[")[1].split(",")[0]
				geo_location_lat = geo_location.split(", ")[1].split("]")[0]

			else:
				geo_location_lat = 'empty'
				geo_location_long = ''

			if(geo_location_lat != 'empty'):
				geo = 'point(' + geo_location_lat + ',' + geo_location_long + ')'

			else:
				return


			date = str(tweet['created_at'])
			date_year = date[26:30]
			date_month = dict[date[4:7]]#for month parsing from dict
			date_day = date[8:10]
			full_date = str(date_day + '/' + date_month + '/' + date_year)

			if hashtags != None:
				if geo != None:
					if full_date != None:


						print hashtags + geo + '  ' + full_date
			return True

#		this exception is for if the keyerror is there are no entities
		except KeyError:
			pass


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
twitterStream.filter(locations = UNITED_STATES+HAWAII+ALASKA) #filters within bound box of USA, including Hawaii and Alaska
