# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:18:03 2018

@author: Kaustav Chatterjee
"""

from textblob import TextBlob
import pandas as pd
T = pd.read_csv('F:/Python_New/Manual_Sentiment.csv')
print(T)
type(T)
FT=T['Formatted_Text']
print(FT)
type(FT)
FT.ix[2]

for i in range(299,401):
    blobpol=TextBlob(FT.ix[i]).sentiment[0]
    blobsub=TextBlob(FT.ix[i]).sentiment[1]
    print(blobpol)
    print(blobsub)
    

    

