# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:43:57 2018

@author: KAUSTAV
"""

names=['ashok','vijay','mahesh']
gender=[0,1,1]

type(names)
type(gender)

names[0]
'ashok'.upper()

email_id = 'clin'
if "@" not in email_id:
    email_id += '@braindeis.edu'
email_id  
  
line = "# This is a comment line \n"
line
line.strip()  
line.rstrip()

city_pop = {"NYC":8550405, "LA":456512, "CHI":3435435678}
city_pop["NYC"]

from scipy.stats.stats import pearsonr
a=[1,4,6]
b=[1,2,3]
print(pearsonr(a,b))

