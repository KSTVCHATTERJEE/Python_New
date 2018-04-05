# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:17:23 2018

@author: Kaustav Chatterjee
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "785355159060684801-enx1HVQxOSgWHCMP2LIfjWiOJHzTUUM"
access_token_secret = "NRgyQoVxZGJeGYJz31RJNhX0EnmFApaG4A0UT2sBEgYUF"
consumer_key = "nZJgglsuEdEjia78QQBS5yrfq"
consumer_secret = "1MJWnrZaf7TtPqZsKw8XI4tKoVQPa9Evc7sN7CeeLquWyzV0HF"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet=json.loads(data)
        print (tweet['created_at'],"\t",tweet['user']['screen_name'],"\t",tweet['geo'], "\t",tweet['text'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Paytm'])