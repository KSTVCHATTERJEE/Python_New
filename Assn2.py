# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:58:09 2018

@author: KAUSTAV
"""
import numpy as np
import pandas as pd
import csv
import statsmodels.api as sm

dataset=pd.read_csv('Contriesdata.csv')
dataset.head()

y=dataset['Population']
x=dataset['Literacy']
x
y.fillna(0)
x.fillna(0)

#Simple Linear Regresion between Popln.and Literacy
model=sm.OLS(y,x).fit()
model.summary()

""" OLS Regression Results                            
==============================================================================
Dep. Variable:             Population   R-squared:                       0.092
Model:                            OLS   Adj. R-squared:                  0.079
Method:                 Least Squares   F-statistic:                     7.303
Date:                Fri, 23 Feb 2018   Prob (F-statistic):            0.00858
Time:                        23:26:27   Log-Likelihood:                -1480.5
No. Observations:                  73   AIC:                             2963.
Df Residuals:                      72   BIC:                             2965.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Literacy    5.477e+05   2.03e+05      2.702      0.009    1.44e+05    9.52e+05
==============================================================================
Omnibus:                      147.510   Durbin-Watson:                   1.955
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            10409.594
Skew:                           7.365   Prob(JB):                         0.00
Kurtosis:                      59.616   Cond. No.                         1.00
==============================================================================

"""
""" R-square is 0.092 which means only 9.2% of variation of Population is explained by Literacy

Adjusted R-sq is 0.079.  Difference between R-sq and adjusted R-sq is high, signifying model is not good. 

Durbin-Watson 1.955 < 2. Proves autocorrelation is present.
"""



#ANOVA between Population and Literacy
from scipy import stats
stats.f_oneway(x,y)

"""Out[71]: F_onewayResult(statistic=7.5771221012572667, pvalue=0.006672737405294585)
F-statistic : 7.58
p-value : 0.006 < 0.05, so we accept null hypothesis and thus can say that there is no significant difference between means of twopopulations y(Population) and x(Literacy). """

"""LR gives more info than ANOVA
ANOVA just compares two popls.
LR tries to create a relationship between two variables using an equation."""
