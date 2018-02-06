# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:38:54 2018

@author: KAUSTAV
"""

import numpy as np
a=np.array([[1,2,3],[4,5,6]],float)
a.shape
a.size
print(a)
print(a.shape,"\n",a.itemsize)
print(a.dtype,a.dtype.type)
type(a[0,0]) is type(a[1,2])

a=np.arange(0,80,10)
a
y=a[[1,2,-3]]
print(y)

y1=[a[1],a[2],a[-3]]
print(y1)

y=np.take(a,[1,2,-3])
print(y)

type(y) is type(y1) #False

ind=[1,2,-3]
y=np.take(a,ind)
print(y)

mask=np.array([0,1,1,0,0,1,0,0],dtype=bool)
y=a[mask]
print(y)


y=np.compress(mask,a)
print(y)

mask2=np.array([True,False,False,False,True,False,True,True],dtype=bool)
y=a[mask2]
print(y)

a=np.array(np.arange(36).reshape(6,6))
a

a[(0,1,2,3,4),(1,2,3,4,5)]

a[3:,[0,2,5]]

mask=np.array([1,0,1,0,0,1],dtype=bool)
mask
a[mask,2]

a=np.array([[1,2,3],[4,5,6]],float)
a
np.sum(a) #Total Sum
a.sum() #Total Sum

sum(a)#Columnwise Sum 
a.sum(axis=0) #Columnwise Sum

a.sum(axis=1) #Rowwise Sum

a.prod()

a.prod(axis=0)

a.prod(axis=1)


a=np.array([2.,3.,0.,1.])
a.min(axis=0)
np.amin(a,axis=0)
a.argmin(axis=0)

np.amax(a,axis=0)
np.amax(a,axis=None)

a=np.array([2.,1.,0.,3.])
a.max(axis=0)

a.argmax(axis=0)

a.mean(axis=0)
np.average(a, weights=[1,2], axis=0)
a.std(axis=0)

a.var(axis=0)

a=np.array([[1,2,3],[4,5,6]], float)
a.clip(3,5)

a=np.array([1.35,2.5,1.5])
a.round()
a.round(decimals=1)

a.ptp(axis=0)

a.ptp(axis=None)

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
a+b

x=np.arange(11.)
x

pi=3.14
a = (2*pi)/10
a
a*x

x*=a
x

y=np.sin(x)
print(y)

a=np.array(((1,2,3,4),(2,3,4,5)))
b=np.array(((1,2,5,4),(1,3,4,5)))
a==b

np.equal(a,b)

#using timeit func to check execution time
%timeit sum(a)
%timeit a.sum()
%timeit np.sum(a)

a.flatten()
type(a.flatten())

b=a.ravel()

a.resize(3,2)
a

id(a)
id(b)

a.swapaxes(0,1)
a

p=np.array([1,2,3,4,5,6]).reshape(2,3)
print(p)

a.T
np.squeeze(a)

x=np.array([[[0],[1],[2]]])
x.shape

np.squeeze(x)

np.squeeze(x).shape