# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:13:41 2018

@author: KAUSTAV
"""

import numpy as np
import pandas as pd

rng=np.random.RandomState(42)
rng
marks=pd.Series(rng.randint(50,100,11))
marks

marks1=pd.Series(rng.randint(50,100,11))
marks1

marks==marks1

marks.sum()
round(marks.std(),2)

#Create a dictionary
{'x':1,'y':[1,2]}
dict(x=1,y=[1,2])

df=pd.DataFrame({'A':rng.randint(1,10,6),'B':rng.randint(1,10,6)})
df

df.sum(axis=0) #columnwise sum
df.sum(axis=1)#rowwise sum

round(df.mean(),2)

round(df.mean(axis=1),2)

df.columns

round(df.describe(),2)

df.mean(axis='columns')

['A','B','C']*2
np.repeat(['A','B','C'],[1,2,3])

df1=pd.DataFrame({'key':['A','B','C']*2,'data1':range(6),'data2':rng.randint(0,10,6)},columns=['key','data1','data2'])

df1

df1.groupby('key').sum()

df1.groupby('key').aggregate(['min','max','median'])

df1.groupby('key').aggregate(np.median)

df1.groupby('key').aggregate(np.median,'median') #error

df1.groupby('key').aggregate({'data1':'min','data2':'max'})
df1.groupby('key').aggregate({'data1':'min','data2':['max','min']})

df1.filter(items = ['key','data1'])
df1.filter(like='2',axis=0)
df1.filter(like='0',axis=1)

round(df1.groupby('key').std(),2)

grouped = df1.groupby('key')
grouped
round(df1['data2'].mean(),2)
grouped.filter(lambda x:x['data2'].mean() > 6) #groupwise mean
grouped.filter(lambda x:x['data2'].std() > 4) #groupwise mean

grouped.transform(lambda x:x-x.mean())



x=2
y=3
product=lambda x,y:x*y
product(x,y)

grouped.apply(lambda x:x ['data2']*2)

df1.groupby('key').sum()

df2=df1.set_index('key')
df2

newmap={'A':'Post Graduate','B':'Master of Science','C':'Bachelor of Science'}
newmap

df2.groupby(newmap).sum()

df2.groupby(str.lower).mean()

df2.groupby([str, str.lower, newmap]).mean()

df2.groupby('key').sum().unstack()


