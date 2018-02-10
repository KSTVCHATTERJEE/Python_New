# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:44:16 2018

@author: KAUSTAV
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.plot(x, np.cos(x))

plt.draw()


import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
plt.plot(x, np.sin(x),'-')
plt.plot(x, np.cos(x),'--')

fig=plt.figure()

fig.savefig('myfigure2.png')

!dir *.png

%matplotlib inline
plt.subplot(2,1,1)
plt.plot(x, np.sin(x))

plt.subplot(2,1,2)
plt.plot(x, np.cos(x))

fig, ax = plt.subplots(3)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.tan(x))


%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import numpy as np
fig=plt.figure()
ax=plt.axes()

x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))

plt.plot(x, np.sin(x-4),color='g')

plt.plot(x,x+1,'-g')

plt.plot(x,np.sin(x))

plt.xlim(-1,11)
plt.ylim(-1.5,1.5)

plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend()

x=np.linspace(0,10,30)
y=np.sin(x)

plt.plot(x,y,'o',color='black');


