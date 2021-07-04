import random
import math
import matplotlib.pyplot as plt
#from pylab import *

class dot:
    def __init__(self,index):
        self.connections=[]
        self.maxstate=0
        self.states=[]
        self.state=0
        self.index=index
        self.stateold=0

    def setstates(self,ndots):
        totalstates=1
        for i in range(len(self.connections)):
            #print (dots[self.connections[i]].maxstate)
            totalstates*=((dots[self.connections[i]].maxstate+1))
        print (totalstates)
        for i in range(totalstates):
            self.states.append(0)

    def sim(self):
        stateindex=0
        for i in range(len(self.connections)):
            stateindex+=((dots[self.connections[i]].maxstate+1)**(len(self.connections)-i-1))*dots[self.connections[i]].state   
        self.stateold=self.states[stateindex]
        
#dots=[dot(0),dot(1),dot(2)]

#################### setting part ########################
numberdots=30
maxstate=1
dots=[]
for i in range(numberdots):
    dots.append(dot(i))

for j in range(numberdots):
    
    dots[j].maxstate=maxstate
    

################# connection part #######################

for i in range(numberdots):
    if i<numberdots-2:
        dots[i].connections=[i-2,i-1,i+1,i+2]

dots[numberdots-2].connections=[numberdots-4,numberdots-3,numberdots-1,0]
dots[numberdots-1].connections=[numberdots-3,numberdots-2,0,1]

################## table configurations #################
     
for i in range(numberdots):
    
    randomlist = [random.randint(0,maxstate) for j in range(16)]
    
    dots[i].states=randomlist
for i in range(numberdots):
    dots[i].state=0
###############################################################

niter=100

listofstates=[]
for el in dots:
    el.setstates(len(dots))

for el in dots:
    print(el.states)

for i in range(niter):
    for el in dots:
        el.sim()
        
    for el in dots:        
        el.state=el.stateold
    print('********************')
    digitlist=[]
    for el in dots:
        print(el.state, end=" ")
        digitlist.append(el.state)
    listofstates.append(digitlist)    
#################### plot section ###############

print (listofstates)  
for i in range(len(listofstates)):
    for j in range(numberdots):
        if listofstates[i][j]==0:
            plt.scatter(j*1,i,s=2,c='r',alpha=1)
        if listofstates[i][j]==1:
            plt.scatter(j*1,i,s=2,c='b',alpha=1)
        if listofstates[i][j]==2:
            plt.scatter(j*1,i,s=2,c='y',alpha=1)
            
#grid(True)
plt.show()
           
    
        
        
