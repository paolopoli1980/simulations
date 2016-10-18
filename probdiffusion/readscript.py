# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 15:42:11 2016

@author: paolo
"""


import pylab
import numpy as np
 
f1=open("nnodi.txt","r")
stringa=f1.readline()
nnodi=int(stringa)
stringa=f1.readline()
nsteps=int(stringa)
f1.close()
matrix = np.zeros(shape=(nnodi,nsteps))    
f1=open("nodidata.out","r")
listdata=[]
vec=[]

for i in range(nsteps):
    for j in range(nnodi):
        stringa=f1.readline()
        val=float(stringa)
        matrix[j][i]=val
    vec.append(np.exp(-i/600.0))	
f1.close()        

for i in range(nnodi):
    pylab.plot(matrix[i])
pylab.plot(vec)
pylab.show()
    