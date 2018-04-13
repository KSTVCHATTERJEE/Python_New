# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:41:15 2018

@author: Kaustav Chatterjee
"""

import pandas as pd
from textblob import TextBlob
tweet=pd.read_csv('F:/R_in_Action/MS2.csv')

s=[0]*101
s
s2=['a']*100
s2
type(tweet)
tweet.columns=['info','tweet','sentiment']
for i in range(1,101):
    sent=TextBlob(tweet['tweet'].iloc[i]).sentiment[0];
    print(sent);
    s[i-1]=sent;

for j in range(0,100):
    if(s[j]>0):
        s2[j]='Positive';
    elif(s[j]<0):
        s2[j]='Negative';
    else:
        s2[j]='Neutral';
        
s2

c=0
for i in range(0,100):
        if(s2[i] == tweet['sentiment'].iloc[i+1]):
            c=c+1;
c

