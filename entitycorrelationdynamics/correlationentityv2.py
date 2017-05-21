# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:59:56 2016

@author: paolo
"""
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


class entity:
    def __init__(self):
        self.linked_nodes=[]
        self.liststates=[] 
        self.maxspace=0   
        self.state=0
        self.oldstate=0 
	               


def node_association(el,numberofnodes,conta,node):
    listnow=[]
    for i in range(numberofnodes):
        listnow.append(i)
    x=random.randint(el.minspace,el.maxspace)
    cont=0
    for i in range(x):
        y=random.randint(1,numberofnodes-cont-1)
 
        if (len(el.linked_nodes)<el.maxspace) and (len(node[int(listnow[y])].linked_nodes)<node[int(listnow[y])].maxspace) and (listnow[y]!=conta):
            error=0
            for k in el.linked_nodes:
                if k==listnow[y]:
                    print k
                    error=1
            if error!=1:        
                el.linked_nodes.append(int(listnow[y]))
                node[int(listnow[y])].linked_nodes.append(int(conta))
                cont+=1
                del listnow[y]
               
        
            
def association(el,numberofnodes,conta,node,modulo):
    iterations=modulo**len(el.linked_nodes)
    for j in range(iterations):
        casual=random.randint(0,modulo-1)
        el.liststates.append(casual)
    
def running(el,numberofnodes,conta,node,modulo):
    somma=0
    for j in range(len(el.linked_nodes)):
        somma=node[el.linked_nodes[j]].oldstate*modulo**j+somma
    el.state=el.liststates[somma]
    
        
def func(t,a,b,c):
    return a*np.exp(-(t*b)/c)*t/c

    
#*******************************************            
node=[]                
listnumb=[]
numberofnodes=5
maxspace=4
minspace=4
modulo=2
dim=numberofnodes
xx=[]
yy=[]
numbassociated=[]
statechosen=1
#numberofiterations=modulo**numberofnodes
numberofiterations=32

print numberofiterations
#numberofiterations=10

for i in range(dim):
    listnumb.append(0)
    xx.append(float((i+1))/float(dim))
    yy.append(0)

for i in range(numberofnodes):
    node.append(entity()) 
           
cont=0 
for el in node:
    x=random.randint(minspace,maxspace)
    el.maxspace=maxspace
    el.minspace=minspace	
conta=0
    
for el in node:
    node_association(el,numberofnodes,conta,node)
    conta+=1
    
cont=0    
for el in node:
    el.linked_nodes=list(set(el.linked_nodes))

 
for el in node:
    el.linked_nodes=list(set(el.linked_nodes))
   
for el in node:
    print el.linked_nodes

for el in node:
    association(el,numberofnodes,conta,node,modulo)
    
#for el in node:
 #   print el.liststates

for el in node:
    el.state=random.randint(0,modulo-1) 
    el.oldstate=el.state       

for t in range(numberofiterations):
    #print "**************************************"
    for el in node:
        running(el,numberofnodes,conta,node,modulo)
    for el in node:
        el.oldstate=el.state 
    c=0    
    numb=0
    for el in node:
        
        numb+=el.state*modulo**(c)
        c+=1
    numbassociated.append(numb)    
#        print el.state
    cont=0    
    for el in node:
        listnumb[cont]=el.state
        cont+=1
    c=-1
    for k in range(dim):
        if listnumb[k]==statechosen:
            c+=1
    if c>=0:
        yy[c]+=1  
   # print "*"	   
#    for el in node:
#	print el.state        
	
print xx
print yy
maximum=0
for el in yy:
    if maximum<float(el):
        maximum=float(el)
for i in range(len(yy)):
    yy[i]=yy[i]/float(maximum)    
plt.plot(xx, yy, 'ro')
plt.axis([0, 1, 0, 1])


plt.show()
plt.plot(numbassociated)
plt.show()

popt, pcov = curve_fit(func, xx, yy)

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