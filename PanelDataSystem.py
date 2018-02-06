# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:39:41 2018

@author: KAUSTAV
"""

import pandas as pd
s=pd.Series([3,7,4,4,0.3],['a','b','c','d','d'])
s
df=pd.DataFrame(np.arange(9).reshape(3,3),['b','a','c'],['Paris','Berlin','Madrid'])
df

data={'Paris':[0,3,6,999999999],'Berlin':[1,4,7],'Madrid':[2,5,8]}
data

df=pd.DataFrame(data,['b','a','c','d'],['Paris','Berlin','Madrid'])

s['b']
s['a':'c']
s['d']
s[1]

df[:2]
df[1:2]

df[df['Paris']>1]
df['Paris']

p=df.Berlin[df['Berlin']>1]
p

df

df.ix['c','Paris']

df.ix['a',['Berlin','Madrid']]

df.drop('c')

s.drop('d')

s.drop_duplicates()

s

df.drop('c')

df.drop('Berlin',axis=1)

s=pd.Series([3.0,7.0,4.0,4.0,0.3],['a','b','c','d','e'])
s
s2=pd.Series([0,1,2],['a','c','f'])
s2

s+s2 #Inner join

s.add(s2,fill_value=0)

df1=pd.DataFrame(np.arange(9).reshape(3,3),['b','a','c'],['Paris','Berlin','Madrid'])
df1

df2=pd.DataFrame(np.arange(12).reshape(4,3),['b','e','c','a'],['Paris','Lisbon','Madrid'])
df2

df1+df2

df.add(df2,fill_value=0)

df3=pd.DataFrame({'data1':[0,1,2,3,4,5,6],'keyLeft':['b','b','a','c','a','a','b']})

df3

df4=pd.DataFrame({'data2':[0,1,2,30],'key':['a','b','d','a']})

df4

pd.merge(df3,df4,left_on = 'keyLeft',right_on='key',how='inner')

pd.merge(df3,df4,left_on='keyLeft', right_on='key', how='outer')

left1=pd.DataFrame({'key':['a','b','a','a','b','c'],'data1':[0,1,2,3,4,5]})
left1

right1=pd.DataFrame({'data2':[0,1,2,3,4],'key':['a','b','a','b','d']})
right1

pd.merge(left1,right1,on='key',how='left')

pd.merge(left1,right1,on='key',how='right')

s

s.rank()

s.rank(method='first')

s.rank(method='max',ascending=False)

df

df.rank()

df.rank(axis=1)

s.sort_index(ascending=False)

df.sort_index(ascending=True)
df.sort_index(by='Berlin')
df.sort_index(axis=1)

df.max()

df+df.max()

import math
f=lambda x: math.sqrt(x)
df.applymap(f)


df.Berlin=df['Berlin'].map(f)
df

df.describe()

df.sum(axis=1)

df.corr()
df.cov()

df

df.reindex(['c','b','a','g'])

df.reindex(['c','b','a','g'],fill_value=14)

df.reindex(columns = ['Varsovie','Paris','Madrid'])



