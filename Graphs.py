# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:54:25 2018

@author: KAUSTAV
"""

import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
x
y
plt.plot(x,y)
plt.show()

x1=[1,2,3]
y1=[2,4,1]
x2=[1,2,3]
y2=[4,1,3]

plt.plot(x1,y1,label='Line1')
plt.plot(x2,y2,label='Line2')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Two lines on the same plot')
plt.show()

plt.bar(x1,y1,tick_label=tick_label,width=0.8,color=['red','green'])
tick_label=['One','Two','Three']

marks=np.random.uniform(30,100,1000)
marks
np.all(marks>=30)
np.all(marks<100)

range=(20,100)

type(range)

bins=10

plt.hist(marks,bins,range, color='green', edgecolor='black', histtype='bar',rwidth=1.4)
plt.xlabel('Marks')
plt.ylabel('No. of students')
plt.title('Histogram of Marks of Students')

x,y

plt.scatter(x,y)
plt.scatter(x,y,label='stars',color='red',marker='*')

plt.pie(y)

plt.pie(y,labels=['sleep','study','eat'],colors=['red','green','yellow'])

plt.pie(y,labels=['sleep','study','eat'],colors=['red','green','yellow'],startangle=90, shadow=True, radius=1.2, explode=(0.5,0.0,0.0), autopct = '%1.1f%%')

