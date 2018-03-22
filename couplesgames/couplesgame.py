from __future__ import division
from visual import *
import random
import math
import matplotlib.pyplot as plt


class point():
    def __init__(self,n):
        self.c=[float(random.uniform(-1,1)) for i in range(n)]
        self.p=[float(random.uniform(-1,1)) for i in range(n)]
        self.index=n
        self.min=1000000
        self.pointer=0
        self.formed=0
    def compare(self):
 
        for i in range(len(obj)):
            if obj[i].formed==1 and self.pointer==i:
                self.min=1000000
 
        if self.formed==0:
            for i in range(len(obj)):
 
                if i!=self.index and obj[i].formed==0:
                    val=0
                    for j in range(n):
                        val+=math.fabs(self.c[j]-obj[i].p[j])
 
                    if val<self.min:
 
                        self.pointer=i
                        self.min=val
 

    def perturb(self,incmax):
        for h in range(len(self.p)):
            cas=random.uniform(-incmax,incmax)
            self.p[h]+=cas
      
         
        
        
ncouples=20
obj=[]
n=2
incmax=0.15
niter=10000
forcop=[]
nfor=[]
connections=[]
connectdist=[]
boxside=10
size=10
node=[]
arrow=[]
points=[]
def build_einv():
    pass


for i in range(2*ncouples):
    obj.append(point(n))
    print obj[i].c    
    print obj[i].p
    print("***************************")
    obj[i].index=i
    x=random.uniform(-5,5)
    y=random.uniform(-5,5)
    z=random.uniform(-5,5)
    
    
    node.append(sphere(pos=vector(x,y,z),radius=0.5))

 

for i in range(len(obj)):
    obj[i].index=i

for s in range(niter):
    rate(400)
    for el in obj:
        el.compare()
    for i in range(len(obj)):
        for k in range(len(obj)):
            if i!=k and obj[i].formed==0  and obj[k].formed==0:
                if obj[i].pointer==obj[k].index and obj[k].pointer==obj[i].index:
                    forcop.append([obj[k].index,obj[i].index])
                    obj[k].formed=1
                    
                    obj[i].formed=1
                    xval=0
                    xval2=0
                    for j in range(n):
                        xval+=math.fabs(obj[k].c[j]-obj[i].p[j])
                        xval2+=math.fabs(obj[k].p[j]-obj[i].c[j])

                    connectdist.append([xval,xval2,1])    
    for el in obj:
        el.perturb(incmax)
    nfor.append(len(forcop))
    if s==0:
        for t in range(len(obj)):

            points.append(cylinder(pos=vector(node[t].pos[0],node[t].pos[1],node[t].pos[2]),axis=vector(node[obj[t].pointer].pos[0],node[obj[t].pointer].pos[1],node[obj[t].pointer].pos[2]), radius=0.05,color=color.green))
    if s!=0:
        
        for t in range(len(obj)):
            points[t].axis=vector(node[obj[t].pointer].pos[0]-points[t].pos[0],node[obj[t].pointer].pos[1]-points[t].pos[1],node[obj[t].pointer].pos[2]-points[t].pos[2])
            if obj[t].formed==1:
                points[t].color=color.red
                points[obj[t].pointer].color=color.red
                node[t].color=color.red
                node[obj[t].pointer].color=color.red
print forcop
print "******************************"
pointstr=""
c=0
for el in obj:
 
    pointstr=str(pointstr)+str(c)+str("->")+str(el.pointer)+str(",")
    c+=1
 
        
 

                  
print connections
print pointstr
print connectdist
plt.plot(nfor)
plt.show()
plt.plot(connectdist)
plt.show()

