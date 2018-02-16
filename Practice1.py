# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:10:32 2018

@author: KAUSTAV
"""

import numpy as np
rollnoL = [109,102,105,106,103,110,101,107,104,111,108]
nameL=['meena','apoorva','kaustav','shubham','goldie','hitesh','shruti',
       'vijay','achal','lalit','varun']
genderL=['F','F','M','M','M','M','F','M','M','M','M']
pythonL=np.random.randint(60,90,11)
print(pythonL)
sasL=np.random.randint(50,100,11)
print(sasL)

import pandas as pd

nameS=pd.Series(nameL, index=rollnoL)
print(nameS)

nameS=pd.Series(nameL)
nameS.index=rollnoL

112 in nameS
111 in nameS

nameS.index
nameS.keys()

nameS.items

nameS.values

list(nameS.items())

nameS[108]='jain'
nameS

nameS[nameS=='jain']

nameS=='jain'

nameS[0:5]
nameS.iloc[0:5]

nameS[109]
nameS.loc[109]
nameS.iloc[0]

nameS[0:1]

nameS.loc[103:110]

nameS.loc[108]
nameS.ix[108]

df=pd.DataFrame(nameS)

rollnoS=pd.Series(rollnoL)
nameS=pd.Series(nameL)
genderS=pd.Series(genderL)
pythonS=pd.Series(pythonL)
sasS=pd.Series(sasL)

studentDF=pd.concat([rollnoS,nameS,genderS,pythonS,sasS],axis=1)

studentDF

studentDF1=pd.DataFrame({'rollno':rollnoL,'name':nameL,'gender':genderL,'python':pythonL,'sas':sasL})

studentDF1.index=rollnoL
studentDF1

studentDF3=pd.DataFrame({'rollno':rollnoL,'sname':nameL,'gender':genderL,'python':pythonL,'sas':sasL},columns=['rollno','sname','gender','python','sas'])

studentDF3.index=rollnoL
studentDF3

studentDF3.values
studentDF3.dtypes

studentDF3.T

studentDF3.values[0]

studentDF3.iloc[0:1]

studentDF3['sname']

studentDF3.iloc[:3,:2]

studentDF3.loc[:105,:'python']

studentDF3.iloc[:5,:2]


studentDF3['total']=studentDF3['python']+studentDF3['sas']
studentDF3.iloc[:5]
studentDF3.head()

studentDF3[studentDF3['total']>150]

studentDF3[studentDF3.total>150]


