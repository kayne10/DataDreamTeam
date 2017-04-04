import ConfigParser
import tweepy
from tweepy import OAuthHandler
import json
import simplejson
from tweepy import Stream
from tweepy.streaming import StreamListener

from datetime import datetime
import os



# Read config file to access API keys
cfg = ConfigParser.ConfigParser()
cfg.read('config.ini')
tweepy_ckey = cfg.get('Tweepy_Keys','ckey')
tweepy_csecret = cfg.get('Tweepy_Keys','csecret')
tweepy_atoken = cfg.get('Tweepy_Keys','atoken')
tweepy_asecret = cfg.get('Tweepy_Keys','asecret')

auth = OAuthHandler(tweepy_ckey, tweepy_csecret)
auth.set_access_token(tweepy_atoken, tweepy_asecret)

index = datetime.now()
date =  index.strftime('%Y%m%d')
json_file = 'tweets' + str(date)

if not os.path.exists('Datasets'):
    os.makedirs('Datasets')


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('./Datasets/'+json_file, 'a') as file:
                file.write(data)
                print json.loads(data)['text'] #['entities']['hastags']
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

# filter array for specific tweets
keywords = ['hiring','hire','jobs']

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=keywords)
