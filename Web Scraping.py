# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:27:16 2018

@author: KAUSTAV 

"""


import tweepy
import json

consumer_key = 'nZJgglsuEdEjia78QQBS5yrfq'
consumer_secret = '1MJWnrZaf7TtPqZsKw8XI4tKoVQPa9Evc7sN7CeeLquWyzV0HF'
access_token = '785355159060684801-enx1HVQxOSgWHCMP2LIfjWiOJHzTUUM'
access_token_secret = 'NRgyQoVxZGJeGYJz31RJNhX0EnmFApaG4A0UT2sBEgYUF'

# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Python'])