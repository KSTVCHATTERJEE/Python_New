# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:07:24 2018

@author: KAUSTAV
"""

numbers=[]
for i in range(1,101):  
    numbers.append(i)

print(numbers)

min(numbers)
max(numbers)
len(numbers)

numbers.sort()
numbers[1]
numbers[-2]

import numpy as np
np.mean(numbers)
np.average(numbers)
np.median(numbers)

#Mean without numpy
i=0
for number in numbers:
    i=i+number
    
mean=i/len(numbers)
print(mean)

#Median without numpy
j=int(len(numbers))
j
if j % 2 == 0:
    median = (numbers[int((j/2)-1)]+numbers[int(j/2)])/2
else:
    median = numbers[int((j+1)/2)]

print(median)

n = [1,4,3,1,2]

print(n)

min=n[0]

for i in n:
    if(i < min):
        min=i
min

min2=n[0]

for i in n:
    if((i < min2) and (i > min)):
        min2=i
    
min2

for i in n:
    while(i>min):
        if(i<min2):
            min2=i

min2
    
max1=0
sec_max=0
min1=0
sec_min=99999999
for i in n:
    if(i>max1):
        sec_max=max1
        max1=i
    if(i<min1):
        sec_min=min1
        min1=i
    if(i<sec_min and i>min1):
        sec_min=i
    if(i>sec_max and i<max1):
        sec_max=i
print(str(sec_min) + " " + str(sec_max))
sec_max
max1
sec_min
min1
   



