# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:53:14 2016

@author: paolo
"""
import random
import matplotlib.pyplot as plt
import numpy as np
 
from scipy.optimize import curve_fit

def func(t,a,b,c):
    return a*np.exp(-(t*b)/c)*t/c

listnumb=[]
x=[]
y=[]
dim=12
states=3
random.seed()
repeat=3**12
for i in range(dim):
    listnumb.append(0)
    x.append((i+1)/float(dim))
    y.append(0)
#mu, sigma = 20, 0.1 # mean and standard deviation
#casual=int(sigma * random.randint(1,100) + mu)    
#casual = (np.random.normal(mu, sigma, 10000))

for i in range(repeat):
    for j in range(dim):
          casual=random.randint(1,99)
#          casual=random.randint(1,states)
          if casual>=1:
              mem=1
          if casual>=34:
              mem=2
          if casual>=95:
              mem=3
#          if casual>=75:
 #             mem=4

          casual=mem    
          listnumb[j]=casual
          #print casual
    c=-1
    for k in range(dim):
        if listnumb[k]==3:
            c+=1
    if c>=0:
        y[c]+=1 
#print y    
 
maximum=0
for el in y:
    if maximum<float(el):
        maximum=float(el)
        
for i in range(len(y)):
    y[i]=y[i]/float(maximum)    
plt.plot(x, y, 'ro')
plt.axis([0, 1, 0, 1])


plt.show()
popt, pcov = curve_fit(func, x, y)

print popt[0]
print popt
t = np.arange(0.0, 1.0, 0.01)
s = popt[0]*np.exp(-(t*popt[1])/popt[2])*t/popt[2]
plt.plot(t, s)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()

 
#fittare con exp(-x/a)/a        
            