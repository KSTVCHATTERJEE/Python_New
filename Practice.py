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