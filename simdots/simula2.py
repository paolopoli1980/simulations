import dots
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n=4
dotsx=[]
maxstate=2
for i in range(n):
    dotsx.append(dots.dot(i))

for j in range(n):
    
    dotsx[j].maxstate=maxstate
dotsx[0].state=2
dotsx[1].state=0
dotsx[2].state=1
dotsx[3].state=2

dotsx[0].connections=[1,2]
dotsx[1].connections=[0,2,3]
dotsx[2].connections=[0,1,2]
dotsx[3].connections=[0,1]

dotsx[0].states=[1,2,0,2,0,1,0,1,2]
dotsx[1].states=[2,0,1,0,0,1,0,1,1,2,0,1,0,0,1,0,1,1,2,0,1,0,0,1,0,1,1,2,0,1,0,0,1,0,1,1]
dotsx[2].states=[0,1,2,1,1,1,0,0,1,0,1,2,1,1,1,0,0,1,0,1,2,1,1,1,0,0,1,0,1,2,1,1,1,0,0,1]
dotsx[3].states=[1,2,1,2,0,0,1,0,1]
niter=10
listofstates=[]

simdot=dots.simdot()

liststates=simdot.simdots(niter,dotsx).copy()
print (liststates)
#print (liststates)
#fig = plt.figure(figsize=(15, 15))
p=[[],[],[],[],[],[],[],[],[],[]]
for i in range(len(liststates)):

    #print(i)
    for j in range(len(liststates[i])):
        p[j].append(liststates[i][j])
plt.plot(p[0])
plt.plot(p[1])
plt.plot(p[2])
plt.plot(p[3])

print('********')
print(p[0])    
plt.show()    

n=4
qdotsx=[]

for i in range(n):
    qdotsx.append(dots.qdot(i))

#for i in range(n):
    #qdotsx[i].state=[.6,0.4]
    #qdots[i].stringstate=['0','1']
'''
qdotsx[0].state=[0.7,0.3]
qdotsx[1].state=[0.8,0.2]
qdotsx[2].state=[0.2,0.8]
qdotsx[3].state=[0.5,0.6]
'''
qdotsx[0].state=[0.2,0.2,0.6]
qdotsx[1].state=[0.7,0.2,0.1]
qdotsx[2].state=[0.1,0.8,0.1]
qdotsx[3].state=[0.1,0.2,0.7]

for j in range(n):
    
    qdotsx[j].maxstate=maxstate

for i in range(n):
    qdotsx[i].state=qdotsx[i].state/np.linalg.norm(qdotsx[i].state)
    
qdotsx[0].connections=[1,2]
qdotsx[1].connections=[0,2,3]
qdotsx[2].connections=[0,1,2]
qdotsx[3].connections=[0,1]

qdotsx[0].states=[1,2,0,2,0,1,0,1,2]
qdotsx[1].states=[2,0,1,0,0,1,0,1,1,2,0,1,0,0,1,0,1,1,2,0,1,0,0,1,0,1,1,2,0,1,0,0,1,0,1,1]
qdotsx[2].states=[0,1,2,1,1,1,0,0,1,0,1,2,1,1,1,0,0,1,0,1,2,1,1,1,0,0,1,0,1,2,1,1,1,0,0,1]
qdotsx[3].states=[1,2,1,2,0,0,1,0,1]

#qdots[0].connections=[1,2,3]
#qdots[1].connections=[0,1,2]
#qdots[2].connections=[0,1,2]

#qdots[0].states=[1,0,1,0]
#qdots[1].states=[1,0,0,1]
#qdots[2].states=[1,1,0,1]

niter=10
liststates=[]
simqd=dots.simqdot()
liststates=simqd.simqdots(niter,qdotsx).copy()
print (liststates)
for el in liststates:
    print(el)
print (liststates)
p=[[],[],[],[],[],[],[],[],[],[]]
for i in range(len(liststates)):
    #print(el)
    
    for j in range(len(liststates[i])):
        p[j].append(liststates[i][j][0]**2)
plt.plot(p[0])
plt.plot(p[1])
plt.plot(p[2])
plt.plot(p[3])



plt.show()    
