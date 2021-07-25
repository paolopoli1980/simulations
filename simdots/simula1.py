import dots
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n=10
dotsx=[]
maxstate=1

for i in range(n):
    dotsx.append(dots.dot(i))
    dotsx[i].state=0
    dotsx[i].maxstate=1

for i in range(2,n-2):
    dotsx[i].connections=[i-2,i-1,i+1,i+2]

dotsx[0].connections=[n-2,n-1,1,2]
dotsx[1].connections=[n-1,0,2,3]

dotsx[n-2].connections=[n-4,n-3,n-1,0]

dotsx[n-1].connections=[n-3,n-2,0,1]


dotsx[0].states=[0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1]
dotsx[1].states=[0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0]
dotsx[2].states=[1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0]
dotsx[3].states=[1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1]
dotsx[4].states=[1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1]
dotsx[5].states=[1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1]
dotsx[6].states=[0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1]
dotsx[7].states=[1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1]
dotsx[8].states=[1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1]
dotsx[9].states=[1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0]


niter=50

simdot=dots.simdot()
liststates=simdot.simdots(niter,dotsx).copy()
print (liststates)
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
plt.plot(p[4])
plt.plot(p[5])
plt.plot(p[6])
plt.plot(p[7])
plt.plot(p[8])
plt.plot(p[9])

print('********')
print(p[0])    
plt.show()    

qdotsx=[]
maxstate=1

for i in range(n):
    qdotsx.append(dots.qdot(i))
    a=random.uniform(0,1)
    b=random.uniform(0,1)
    
    qdotsx[i].state=[a,b]
    qdotsx[i].maxstate=1
    qdotsx[i].state/=np.linalg.norm(qdotsx[i].state)

'''
for i in range(n):
    qdotsx.append(dots.qdot(i))
    qdotsx[i].state=0
    qdotsx[i].maxstate=1
'''
for i in range(2,n-2):
    qdotsx[i].connections=[i-2,i-1,i+1,i+2]

qdotsx[0].connections=[n-2,n-1,1,2]
qdotsx[1].connections=[n-1,0,2,3]

qdotsx[n-2].connections=[n-4,n-3,n-1,0]

qdotsx[n-1].connections=[n-3,n-2,0,1]

qdotsx[0].states=[0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1]
qdotsx[1].states=[0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0]
qdotsx[2].states=[1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0]
qdotsx[3].states=[1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1]
qdotsx[4].states=[1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1]
qdotsx[5].states=[1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1]
qdotsx[6].states=[0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1]
qdotsx[7].states=[1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1]
qdotsx[8].states=[1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1]
qdotsx[9].states=[1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0]



'''

qdotsx[0].state=[1,0.]
qdotsx[1].state=[1,0]
qdotsx[2].state=[1,0.]
qdotsx[3].state=[1,0.]
qdotsx[4].state=[1,0]
qdotsx[5].state=[1,0.]
qdotsx[6].state=[1,0.]
qdotsx[7].state=[1,0.]
qdotsx[8].state=[1,0.]
qdotsx[9].state=[1,0.]
'''
niter=50

liststates=[]
simqd=dots.simqdot()
liststates=simqd.simqdots(niter,qdotsx).copy()
print (liststates)
p=[[],[],[],[],[],[],[],[],[],[]]
for i in range(len(liststates)):
    #print(el)
    
    for j in range(len(liststates[i])):
        p[j].append(liststates[i][j][1]**2)
plt.plot(p[0])
plt.plot(p[1])
plt.plot(p[2])
plt.plot(p[3])
plt.plot(p[4])
plt.plot(p[5])
plt.plot(p[6])
plt.plot(p[7])
plt.plot(p[8])
plt.plot(p[9])

plt.show()    

