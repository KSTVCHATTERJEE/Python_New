# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:34:24 2018

@author: KAUSTAV
"""

rollnoL = [109,102,105,106,103,110,101,107,104,111,108]
nameL=['meena','apoorva','kaustav','shubham','goldie','hitesh','shruti',
       'vijay','achal','lalit','varun']
genderL=['F','F','M','M','M','M','F','M','M','M','M']
pythonL=np.random.randint(60,90,11)
sasL=np.random.randint(65,85,11)
hadoopL=np.random.randint(71,90,11)
feesL=np.random.randint(100000,150000,11)
hostelL=[True,False,True,False,False,False,False,True,True,True,False]
courseL=['pg','pg','msc','msc','pg','pg','pg','pg','pg','pg','bsc']
print(rollnoL)
print(nameL)
print(genderL)
print(pythonL)
print(sasL)
print(hadoopL)
print(feesL)
print(hostelL)
print(courseL)

import pandas as pd studentDF=pd.DataFrame({'rollno':rollnoL,'name',:nameL,'gender':genderL,'python':pythonL,'sas':sasL,'hadoop':hadoopL,'fees':feesL,'hostel':hostelL,'course':courseL})

rollnoS=pd.Series(rollnoL)
nameS=pd.Series(nameL)
genderS=pd.Series(genderL)
pythonS=pd.Series(pythonL)
sasS=pd.Series(sasL)
hadoopS=pd.Series(hadoopL)
feesS=pd.Series(feesL)
hostelS=pd.Series(hostelL)
courseS=pd.Series(courseL)

studentDF=pd.concat([rollnoS,nameS,genderS,pythonS,sasS,hadoopS,feesS,hostelS,courseS],axis=1)
studentDF.columns=['rollno','name','gender','python','sas','hadoop','fees','hostel','course']
studentDF

studentDF.to_csv("students2.csv",index=False)

studentDF.groupby('gender').mean()
studentDF.groupby('gender').sum()

studentDF.groupby('gender').size()
studentDF['python'].groupby('gender').size()

classes=['C1','C2','C3']
from numpy import random
sclassL=random.choice(classes,11)
sclassL
studentDF['sclass']=sclassL
studentDF

studentDF.dtypes

studentDF.to_csv("students.csv",index=False)

pd.pivot_table(studentDF,index=['name'])
pd.pivot_table(studentDF,index=['name','sclass','hostel'])
pd.pivot_table(studentDF,index=['sclass','gender'])

studentDF['total']=studentDF['python']+studentDF['sas']+studentDF['hadoop']

pd.pivot_table(studentDF, index=['course','sclass'],values=['total','python'])


pd.pivot_table(studentDF, index=['course','sclass'],values=['total','python'], aggfunc=np.sum)
import numpy as np
pd.pivot_table(studentDF, index=['course','sclass'],values=['total','python'], aggfunc=[np.sum,np.mean,len])







