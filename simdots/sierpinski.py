import random
import math
import dots
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#################### setting part ########################

numberdots=100
maxstate=1
dotsx=[]
for i in range(numberdots):
    dotsx.append(dots.dot(i))

for j in range(numberdots):
    
    dotsx[j].maxstate=maxstate
    

################# connection part #######################

for i in range(1,numberdots-1):

    dotsx[i].connections=[i-1,i+1]

dotsx[numberdots-1].connections=[numberdots-2,0]
'''
dots[0].connections=[1,2,3]
dots[1].connections=[0]
dots[2].connections=[0,3]
dots[3].connections=[0,1,2]
'''
################## table configurations #################

p=(maxstate+1)
k=0

#for k in range(1):
#    print('**********************************')
#    for i in range(numberdots):
#        if i<2 or i>5:
#            k=0
#        else:
#            k=0
#        randomlist = [random.randint(0,maxstate-k) for j in range(p**6)]
#        dotsx[i].states[:]=randomlist[:]
#

for i in range(numberdots):
    dotsx[i].state=0
    ###############################################################
dotsx[int(numberdots/2)].state=1
for i in range(numberdots):
    dotsx[i].states=[0,1,1,0]
        

    
niter=100
listofstates=[]

simdot=dots.simdot()

liststates=simdot.simdots(niter,dotsx).copy()
#print (liststates)
for i in range(len(liststates)):
    for j in range(numberdots):
        if liststates[i][j]==0:
            plt.scatter(j*0.01,i*2,s=2,c='b',alpha=1)
        if liststates[i][j]==1:
            plt.scatter(j*0.01,i*2,s=2,c='r',alpha=1)
        if liststates[i][j]==2:
            plt.scatter(j*0.01,i*2,s=2,c='y',alpha=1)
        if liststates[i][j]==3:
            plt.scatter(j*0.01,i*2,s=2,c='g',alpha=1)
        if liststates[i][j]==4:
            plt.scatter(j*0.01,i*2,s=2,c='0',alpha=1)            
#grid(True)

#plt.show()
        
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')
dalfa=2*math.pi/numberdots
for i in range(niter):
    alfa=0
    
    for j in range(numberdots):
        
        if liststates[i][j]==0:
            cs='b'
        if liststates[i][j]==1:
            cs='r'
        if liststates[i][j]==2:
            cs='y'            
        if liststates[i][j]==3:
            cs='g'            
        if liststates[i][j]==4:
            cs='o'            
        x=1*math.cos(alfa)
        y=1*math.sin(alfa)
        x2=1*math.cos(alfa+dalfa)
        y2=1*math.sin(alfa+dalfa)

        ax.scatter(x,y,i,color=cs,alpha=1)
        if j+1<numberdots:
            if liststates[i][j]==liststates[i][j+1]:
                ax.plot([x,x2],[y,y2],[i,i],color=cs)
        alfa+=dalfa
ax.set_xlabel('Y Label')
ax.set_ylabel('X Label')
ax.set_zlabel('Z Label')

                        
plt.show()

