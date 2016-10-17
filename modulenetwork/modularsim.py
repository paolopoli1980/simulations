# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 20:42:28 2015

@author: paolo
"""
import pylab
import random
f1=open("rete.dat","r")

dati=f1.readlines()

 
f1.close()

f1=open("val.dat","r")

dati2=f1.readline()

f1.close()

f1=open("mod.dat","r")

dati3=f1.readline()

f1.close()


iteration=input("insert the number of the iterations=") 
print dati2
dati2=dati2.split()
dati3=dati3.split()
print dati3[0]
print dati2[0]
print dati[0][0]
dati2new=[]
dati2back=[]
dati2back[:]=dati2[:] 
#print y[0][0]
limin=0
limax=100
seq=[]
ntry=1
sens=0
eps=2
minimo=1000000000

for i in range(iteration):
    seq.append(random.randint(limin,limax))    
for n in range(ntry):
    dati2[:]=dati2back[:]
    for y in range(len(dati2)):
        eps=random.randint(0,sens)
        
        dati2[y]=int(dati2[y])    
        dati2[y]+=eps
        
    y=[ [ 0 for i in range(iteration) ] for j in range(len(dati2)) ] 
    dati2new[:]=dati2[:]
    for i in range(iteration):
        
        
       # y[i][0]=dati[0]
        
        x=[0]
        dati2[:]=dati2new[:]
        for j in range(len(dati2)):
           
            
             #   print j
                
                somma=0
                #dati2new[:]=dati2[:]
                
                for k in range(len(dati2)):
                
                    if dati[j][k]=="1":
                       #print k
                       somma=somma+int(dati2[k])
                dati2new[j]=somma%int(dati3[j])
               # if n==76:
                   # print "ok"
                #    dati2new[j]=seq[i]+3        
                y[j][i]=dati2new[j]    
                #dati2[:]=dati2new[:]
                
        print dati2
            
            
           #y[i][k]=dati[c2]
 #           x.append(c)
    sommin=0
    for j in range(len(dati2)):
        for i in range(iteration):
            sommin=sommin+abs(int(seq[i])-int(y[j][i]))
        if sommin<minimo:
            minimo=sommin
            print minimo
            
            pointgraph=[]
            for t in range(iteration):
                pointgraph.append(y[j][t])           

#pylab.plot(pointgraph)
#pylab.plot(seq)
print seq
print "lista"
print pointgraph
print minimo
#pylab.show()
                
                
if ntry==1:
    pointgraph=[]  
    start=input("start=")
    end=input("end=")
    for j in range(start,end):        
        for i in range(iteration):
            pointgraph.append(y[j][i])           
        pylab.plot(pointgraph)
            
     #1print pointgraph    
        pylab.show()
        pointgraph=[]    
    pointgraph=[]    
   # pointgraph=[]

print dati
print dati3            
print dati2         
#            pylab.plot(dati2)
            