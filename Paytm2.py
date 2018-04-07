# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 21:49:46 2018

@author: Kaustav Chatterjee
"""

import tweepy
import csv

consumer_key = "nZJgglsuEdEjia78QQBS5yrfq"
consumer_secret = "1MJWnrZaf7TtPqZsKw8XI4tKoVQPa9Evc7sN7CeeLquWyzV0HF"
access_token = "785355159060684801-enx1HVQxOSgWHCMP2LIfjWiOJHzTUUM"
access_token_secret = "NRgyQoVxZGJeGYJz31RJNhX0EnmFApaG4A0UT2sBEgYUF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('tweets2.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="@Paytm",
                           lang="en",
                           since_id="2018-04-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
