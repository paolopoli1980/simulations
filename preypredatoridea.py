# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:02:25 2016

@author: paolo
"""

#prey predator optimizating project
import random
import math
import time
#from __future__ import division
from visual import *  


scene = display(title='Preypredator',
x=0, y=0, width=2000, height=2000,
center=(0,0,0), background=(0,1,1))

class entity:

    def __init__(self):

        self.x=[0,0,0,0,0,0,0,0,0,0]
        self.xforward=[0,0,0,0,0,0,0,0,0,0]
        self.direction=[0,0,0,0,0,0,0,0,0,0]
        self.ndim=0                       
        self.type=""
        self.contator=0
        self.survive=1
        self.selectpredator=-1
        self.mindist=0
        

    def put_entity(self,ndim):
        for i in range(ndim):    
            self.x[i]=random.random()*dimwindow[i]-dimwindow[i]/2
            
                

                    
        
                            
    
             
#scene.autoscale=true
#scene.fillswindow=true
    #scene.autocenter=true
    #scene.range=25   
def move_objects(nentity,ndim,nsteps):
    visualpredators=[]    
    for i in range(nentity):
        if obj[i].tipology=="predator":
            visualpredators.append(pyramid(pos=(obj[i].x[0],obj[i].x[1],obj[i].x[2]), size=(0.2,0.2,0.1),color=color.red,axis=(0.2,0,0)))
        if obj[i].tipology=="prey":
            visualpredators.append(box(pos=(obj[i].x[0],obj[i].x[1],obj[i].x[2]), size=(0.1,0.1,0.1),color=(0,0,255),axis=(1,0,0)))

    f4=open("predatorpos","r")
    f5=open("directions","r")
    f6=open("visible","r")
    
    for j in range(nsteps):
        for i in range(nentity):
            if obj[i].tipology=="predator":
                vis=f6.readline()
                vis=float(vis[0:len(vis)-1])
                if vis==0:
                    visualpredators[i].visible=0
                else:
                    visualpredators[i].visible=1
                
            if obj[i].tipology=="prey":
                vis=f6.readline()
                vis=float(vis[0:len(vis)-1])
                if vis==0:
                    visualpredators[i].visible=0
                else:
                    visualpredators[i].visible=1
            if ((obj[i].tipology=="predator") and (obj[i].survive==1)):

                 
                if ndim==1:
                    stringa1=f4.readline()
                    stringa1=float(stringa1[0:len(stringa1)-1]) 
                    stringa2=0.0
                    stringa3=0.0
                    axix=f5.readline()
                    axix=float(axix[0:len(axix)-1]) 
                    axiy=0.0
                    axiz=0.0

                if ndim==2:
                    stringa1=f4.readline()
                    stringa1=float(stringa1[0:len(stringa1)-1]) 
                    stringa2=f4.readline()
                    stringa2=float(stringa2[0:len(stringa2)-1])
                    stringa3=0.0
                    axix=f5.readline()
                    axix=float(axix[0:len(axix)-1]) 
                    axiy=f5.readline()
                    axiy=float(axiy[0:len(axiy)-1]) 
                    axiz=0.0

                if ndim==3:
                    stringa1=f4.readline()
                    stringa1=float(stringa1[0:len(stringa2)-1])
                    stringa2=f4.readline()
                    stringa2=float(stringa2[0:len(stringa2)-1])
                    stringa3=f4.readline()
                    stringa3=float(stringa3[0:len(stringa2)-1])
                    axix=f5.readline()
                    axix=float(axix[0:len(axix)-1]) 
                    axiy=f5.readline()
                    axiy=float(axiy[0:len(axiy)-1]) 
                    axiz=f5.readline()
                    axiz=float(axiz[0:len(axiz)-1]) 
 
               # print ("try")
  
                
#                   print stringa1
#                    print stringa2
                rate(300)    
                visualpredators[i].pos.x=stringa1
                visualpredators[i].pos.y=stringa2
                visualpredators[i].pos.z=stringa3
                visualpredators[i].axis.x=axix
                visualpredators[i].axis.y=axiy
                visualpredators[i].axis.z=axiz
                


    f4.close()
    f5.close()
    f6.close()  
    f7.close()
    
def print_to_screen(nentity):
    for i in range(nentity):
        for j in range(ndim):
            print obj[i].x[j]

def choose_tipology(nentity,nprey,npredator):
    for i in range(npredator):
        obj[i].tipology="predator"
        print i
    for j in range(nprey):
        obj[i+j+1].tipology="prey"
       # print i+j+1  


def the_best_chance(nentity,index,step,eatingdist,ndim):
    listselect=[]
    dist=0
    for k in range(nentity):
        mindist=10000000000000000000000000000000
        elemento=-1
        if ((obj[k].tipology=="prey") and (obj[k].survive==1)):                
            for l in range(nentity):
                
                dist=0
                if ((obj[l].tipology=="predator") and (obj[l].survive==1) and (k!=l)):
                    for t in range(ndim):
                        dist=dist+(obj[l].x[t]-obj[k].x[t])**2
                    dist=math.sqrt(dist)    
                    if dist<mindist:
                        error=0    
                        for el in listselect:
                            if el==l:
                                error=1
                        if error==0:
                            elemento=l
                            mindist=dist
        if elemento!=-1:      
            obj[k].selectpredator=elemento
            listselect.append(elemento)
            obj[obj[k].selectpredator].mindist=mindist
    dist=0                    
    for k in range(nentity):
        dist=0
        if ((obj[k].tipology=="prey") and (obj[k].survive==1) and (k!=obj[k].selectpredator) and (obj[k].selectpredator!=-1)):
            for t in range(ndim):
                obj[obj[k].selectpredator].direction[t]=(obj[k].x[t]-obj[obj[k].selectpredator].x[t])
               # print obj[obj[k].selectpredator].direction[t]
                
                obj[obj[k].selectpredator].xforward[t]=(obj[k].x[t]-obj[obj[k].selectpredator].x[t])*step/obj[obj[k].selectpredator].mindist                            
                #print (obj[k].x[t]-obj[obj[k].selectpredator].x[t])
                dist=dist+(obj[obj[k].selectpredator].xforward[t]+obj[obj[k].selectpredator].x[t]-obj[k].x[t])**2
            dist=math.sqrt(dist)
           # print dist
            if dist<=eatingdist:
                obj[k].survive=0
                obj[obj[k].selectpredator].contator+=1
                dist=0
    for j in range(nentity):
        if obj[j].tipology=="predator":
            norm=0
            for t in range(ndim):
                norm=obj[j].direction[t]**2+norm
               # print norm
            norm=math.sqrt(norm)
        
        for k in range(ndim):
            if (obj[j].tipology=="predator"):
                if norm!=0:
                    obj[j].direction[k]=obj[j].direction[k]*0.2/norm
                    obj[j].x[k]=obj[j].xforward[k]+obj[j].x[k]
                f1.write(str(obj[j].x[k])+str("\n"))
                f3.write(str(obj[j].direction[k])+str("\n"))
        if ((obj[j].tipology=="prey") or (obj[j].tipology=="predator")):
            f2.write(str(obj[j].survive)+str("\n"))  
            if obj[j].survive==0:
                f4.write("0\n")                                  
            if obj[j].survive==1:
                f4.write("1\n")                                  
              
                                      
def greedy_eachstep(nentity,index,step,eatingdist,ndim):

  
    for j in range(nentity):
        mindist=1000000000000000000000000000000000
        
        if ((obj[j].tipology=="predator") and (obj[j].survive==1)):
            for k in range(nentity):    
                if ((obj[k].tipology=="prey") and (obj[k].survive==1) and (k!=j)):
                    dist=0        
                    for d in range(ndim):
                        dist=dist+(obj[j].x[d]-obj[k].x[d])**2                        
            
                    if dist<mindist:
                        mindist=math.sqrt(dist)
                        #print mindist,j,k
                                
                        for t in range(ndim): 
                            obj[j].direction[t]=-(obj[j].x[t]-obj[k].x[t])
                            obj[j].xforward[t]=-(obj[j].x[t]-obj[k].x[t])*step/mindist
                        if dist<=eatingdist:
                            obj[k].survive=0
                            obj[j].contator+=1
    for j in range(nentity):
        norm=0
        for t in range(ndim):
            norm=obj[j].direction[t]**2+norm
          #  print norm
        norm=math.sqrt(norm)
        
        for k in range(ndim):
            if obj[j].tipology=="predator":
                obj[j].direction[k]=obj[j].direction[k]*0.2/norm
                obj[j].x[k]=obj[j].xforward[k]+obj[j].x[k]
                f1.write(str(obj[j].x[k])+str("\n"))
                f3.write(str(obj[j].direction[k])+str("\n"))
        if ((obj[j].tipology=="prey") or (obj[j].tipology=="predator")):
            f2.write(str(obj[j].survive)+str("\n"))  
            if obj[j].survive==0:
                f4.write("0\n")                                  
            if obj[j].survive==1:
                f4.write("1\n")                                  
                        
                        
#****************Setting initial state****************************** #        
choose=raw_input("Do you want to see the simulation moving graph?(y/n)=")
nentity=200
ndim=2
obj=[]
dimwindow=[10,5]
nprey=80
npredator=120
step=0.01
nsteps=1000
eatingdist=0.01
#******************close initial state session***********************#

for i in range(nentity):
    obj.append(entity())
    
for j in range(nentity):
    obj[j].put_entity(ndim)
    obj[j].survive=1        

choose_tipology(nentity,nprey,npredator)
#********************start simulation*****************************
print_to_screen(nentity)
for i in range(nentity):
    if obj[i].tipology=="predator":
        print "predator"
        print i
    if obj[i].tipology=="prey":    
        print "prey"
        print i    

f1=open("predatorpos","w")
f2=open("lifeprey","w")
f3=open("directions","w")
f4=open("visible","w")
for t in range(nsteps):
    #greedy_eachstep(nentity,i,step,eatingdist,ndim)
    the_best_chance(nentity,i,step,eatingdist,ndim)
f1.close() 
f2.close()
f3.close()
f4.close()

 
if choose=="y":
    move_objects(nentity,ndim,nsteps)    
 




